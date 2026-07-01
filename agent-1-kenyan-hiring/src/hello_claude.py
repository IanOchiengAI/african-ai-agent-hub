"""
Week 1 — First Contact
======================
The simplest possible script: send a message to an AI and print the response.
This confirms your environment is working before we build anything more complex.

We are using Groq (https://console.groq.com) — it's FREE, no credit card needed.
The model we use is Llama 3.3 (made by Meta, hosted by Groq).

Run: python src/hello_claude.py
"""

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
# (This reads your secret GROQ_API_KEY from the .env file you created)
load_dotenv()

# Initialise the Groq client
# Think of this as creating your "phone" with the AI's number already saved
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)


def ask_ai(question: str) -> str:
    """Send a question to the AI and return the response text."""
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # Free, powerful model by Meta
        messages=[
            {"role": "user", "content": question}
        ],
        max_tokens=1024,
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    print("🌍 African AI Agent Hub — Week 1")
    print("Testing connection to Groq API (free tier)...\n")

    # Test: Basic question relevant to our project
    response = ask_ai(
        "I'm building an AI agent to screen CVs for the Kenyan job market. "
        "In two sentences, what's the most important thing I should teach the "
        "AI to understand about the Kenyan education system?"
    )

    print("AI says:")
    print(f"\n{response}\n")
    print("✅ API connection working. Week 1 complete.")
