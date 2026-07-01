"""
base.py — The BaseAgent class
==============================
Every agent in our system is an instance of BaseAgent.

Think of it like ADK's Agent() class:
  - name:          who this agent is
  - system_prompt: its "instruction=" — what it's been told to do
  - model:         which LLM it uses
  - run():         send input, get output (one call)
  - run_with_retry(): the LoopAgent pattern — retry if a checker rejects the output
"""

import os
import json
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console

load_dotenv()
console = Console()

# ── Dual-provider client initialization (Lazy loaded at runtime) ──────────────
provider = None
client = None

def init_client():
    global provider, client
    if client is not None:
        return
    
    groq_key = os.environ.get("GROQ_API_KEY")
    google_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    
    if groq_key:
        from groq import Groq
        provider = "groq"
        client = Groq(api_key=groq_key)
        console.print("[green]Using Groq (Llama 3.3 70B) as the active model provider.[/green]")
    elif google_key:
        provider = "google"
        client = genai.Client(api_key=google_key)
        console.print("[green]Using Gemini 3.5 Flash as the active model provider.[/green]")
    else:
        raise ValueError("Neither GROQ_API_KEY nor GOOGLE_API_KEY / GEMINI_API_KEY found in environment or secrets.")

MODEL = "gemini-3.5-flash"

# High thinking = the model reasons deeply before answering.
# Great for complex extraction and scoring tasks (Gemini only).
THINKING_CONFIG = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
        thinking_level=types.ThinkingLevel.HIGH
    )
)


class BaseAgent:
    """
    The building block for every sub-agent.

    Parameters
    ----------
    name          : Human-readable name shown in logs
    system_prompt : The agent's instructions (like 'instruction=' in ADK)
    """

    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt

    def run(self, user_input: str) -> str:
        """
        Send a message to the active provider and return its text response.

        This is the single LLM call — the "Act" step in the ReAct cycle.
        """
        import time
        console.print(f"  [dim]-> {self.name} thinking...[/dim]")

        global provider, client
        if client is None:
            init_client()

        max_api_retries = 3
        backoff_delay = 2

        for attempt in range(max_api_retries):
            try:
                if provider == "groq":
                    chat_completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": self.system_prompt},
                            {"role": "user", "content": user_input}
                        ],
                        max_tokens=4096,
                    )
                    return chat_completion.choices[0].message.content
                else:
                    response = client.models.generate_content(
                        model=MODEL,
                        contents=[
                            types.Content(role="user", parts=[
                                types.Part(text=f"{self.system_prompt}\n\n{user_input}")
                            ])
                        ],
                        config=THINKING_CONFIG,
                    )
                    return response.text
            except Exception as e:
                error_str = str(e).lower()
                is_transient = False
                
                # Check status code or common error keywords for transient overload
                if hasattr(e, "code") and e.code in (429, 503):
                    is_transient = True
                elif "503" in error_str or "429" in error_str or "overloaded" in error_str or "unavailable" in error_str or "high demand" in error_str:
                    is_transient = True

                if is_transient and attempt < max_api_retries - 1:
                    console.print(f"    [yellow][API WARN] {provider.upper()} is overloaded. Retrying in {backoff_delay}s... (Attempt {attempt+1}/{max_api_retries})[/yellow]")
                    time.sleep(backoff_delay)
                    backoff_delay *= 2
                else:
                    console.print(f"[bold red]API Error in {self.name}: {e}[/bold red]")
                    raise e

    def run_with_retry(
        self,
        user_input: str,
        checker: "BaseAgent",
        max_retries: int = 3
    ) -> str:
        """
        The LoopAgent pattern from the ADK video.

        1. Run this agent to get output
        2. Pass output to checker agent
        3. If checker says "retry" → go back to step 1
        4. If checker says "ok" → return the output
        5. After max_retries → return whatever we have

        This is exactly how ADK's LoopAgent works internally.
        """
        attempt = 0
        output = ""

        while attempt < max_retries:
            attempt += 1
            console.print(f"\n[bold cyan]  [{self.name}] Attempt {attempt}/{max_retries}[/bold cyan]")

            output = self.run(user_input)

            # ── Observe: ask the checker ──────────────────────────────────────
            validation = checker.run(output)
            console.print(f"  [dim]Checker ({checker.name}): {validation.strip()[:80]}[/dim]")

            if "ok" in validation.lower():
                console.print(f"  [green][OK] {self.name} passed validation[/green]")
                return output

            # ── Adjust: retry with feedback ───────────────────────────────────
            console.print(f"  [yellow][RETRY] Retrying — checker said: {validation.strip()[:60]}[/yellow]")
            user_input = f"{user_input}\n\nPrevious attempt failed. Checker feedback:\n{validation}\n\nPlease fix and try again."

        console.print(f"  [red][WARN] {self.name} used all {max_retries} retries[/red]")
        return output
