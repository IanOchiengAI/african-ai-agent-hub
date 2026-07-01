"""
agent.py — Root Agent (The Conductor)
=======================================
This is the top-level orchestrator — equivalent to the Root Agent in the
ADK video. It:

1. Reads the CV file and job description file
2. Runs Stage 1: CV Extraction (with retry loop)
3. Runs Stage 2: Scoring (with retry loop)
4. Runs Stage 3: Report generation
5. Prints the final report to the terminal
6. Saves the report to a file

Usage:
  python src/agent.py --cv data/sample_cvs/sample_1_john_kamau.txt \
                      --job data/sample_job_descriptions/junior_dev.txt

How state flows between agents (the ADK 'output_key' pattern):
  state["cv_text"]  → CVExtractorAgent  → state["cv_data"]
  state["cv_data"]  → ScoringAgent      → state["score"]
  state["score"]    → ReportAgent       → state["report"]
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.rule import Rule
from rich.panel import Panel

# Add src/ to path so we can import agents/
sys.path.insert(0, str(Path(__file__).parent))

from agents.cv_extractor import extract_cv
from agents.scorer import score_candidate
from agents.reporter import generate_report

console = Console()


def run_pipeline(cv_path: str, jd_path: str) -> None:
    """Run the full hiring agent pipeline."""

    # ── Load files ────────────────────────────────────────────────────────────
    cv_text = Path(cv_path).read_text(encoding="utf-8")
    jd_text = Path(jd_path).read_text(encoding="utf-8")

    console.print(Rule("[bold blue]Kenyan Hiring Agent — Starting[/bold blue]"))
    console.print(f"[dim]CV:  {cv_path}[/dim]")
    console.print(f"[dim]Job: {jd_path}[/dim]\n")

    # ── State dict (like ADK's session state) ─────────────────────────────────
    state = {
        "cv_text": cv_text,
        "jd_text": jd_text,
    }

    # ── Stage 1: CV Extraction ────────────────────────────────────────────────
    console.print(Rule("[cyan]Stage 1: CV Extraction[/cyan]"))
    state["cv_data"] = extract_cv(state["cv_text"])
    console.print(f"  [green][OK] Extracted data for: {state['cv_data'].get('name')}[/green]")

    # ── Stage 2: Scoring ──────────────────────────────────────────────────────
    console.print(Rule("[cyan]Stage 2: Scoring[/cyan]"))
    state["score"] = score_candidate(state["cv_data"], state["jd_text"])
    overall = state["score"].get("overall_score", "?")
    rec = state["score"].get("recommendation", "?").upper()
    console.print(f"  [green][OK] Score: {overall}/100 — {rec}[/green]")

    # ── Stage 3: Report ───────────────────────────────────────────────────────
    console.print(Rule("[cyan]Stage 3: Report[/cyan]"))
    state["report"] = generate_report(state["cv_data"], state["score"], state["jd_text"])

    # ── Print final report ────────────────────────────────────────────────────
    console.print(Rule("[bold green]Final Recommendation[/bold green]"))
    console.print(Panel(state["report"], border_style="green"))

    # ── Save report to file ───────────────────────────────────────────────────
    candidate_name = state["cv_data"].get("name", "unknown").replace(" ", "_").lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_path = Path("data") / "reports" / f"{candidate_name}_{timestamp}.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(state["report"], encoding="utf-8")
    console.print(f"\n[dim]Report saved to: {output_path}[/dim]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kenyan Hiring Agent")
    parser.add_argument("--cv",  required=True, help="Path to CV text file")
    parser.add_argument("--job", required=True, help="Path to job description file")
    args = parser.parse_args()

    run_pipeline(args.cv, args.job)
