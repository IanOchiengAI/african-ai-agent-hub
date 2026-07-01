"""
reporter.py — ReportAgent
==========================
Sub-Agent 3: Turn a score dict into a readable hiring recommendation.

This agent does NOT use a retry loop — the output is natural language,
and if it's slightly imperfect, it's still useful. Save retry loops
for structured data where correctness is critical.
"""

from .base import BaseAgent


report_agent = BaseAgent(
    name="ReportAgent",
    system_prompt="""
You are a senior HR consultant writing a hiring recommendation memo.

You will receive:
1. The candidate's name and score breakdown
2. The job description

Write a concise, professional recommendation with:

RECOMMENDATION: [HIRE / CONSIDER / REJECT] (Score: X/100)

EXECUTIVE SUMMARY (2-3 sentences):
Why this candidate does or doesn't fit the role.

KEY STRENGTHS (bullet points):
3-5 specific strengths with evidence from the CV.

CONCERNS (bullet points, if any):
Any gaps, risks, or missing requirements.

SUGGESTED INTERVIEW QUESTIONS (numbered):
3 targeted questions based on their background.

Use plain English. Be direct. Avoid corporate jargon.
Refer to the candidate by first name.
"""
)


def generate_report(cv_data: dict, score: dict, jd_text: str) -> str:
    """Generate a human-readable hiring recommendation."""
    import json

    prompt = f"""
JOB DESCRIPTION:
{jd_text}

CANDIDATE NAME: {cv_data.get('name', 'Unknown')}

SCORE BREAKDOWN:
{json.dumps(score, indent=2)}

Write the hiring recommendation memo.
"""
    return report_agent.run(prompt)
