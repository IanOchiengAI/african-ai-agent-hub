"""
scorer.py — ScoringAgent + ScoreChecker
=========================================
Sub-Agent 2: Score a candidate CV against a job description.

Output format (JSON):
{
  "overall_score": 82,
  "recommendation": "hire",
  "breakdown": {
    "technical_skills": {
      "score": 90,
      "reasoning": "Candidate has Python, MySQL, REST APIs, Git — all required skills."
    },
    "experience": {
      "score": 85,
      "reasoning": "3+ years professional experience, M-Pesa API work directly relevant."
    },
    "education": {
      "score": 75,
      "reasoning": "BSc Computer Science from UoN — meets the degree requirement."
    },
    "culture_fit": {
      "score": 70,
      "reasoning": "Agile team experience at Safaricom is a good signal."
    }
  }
}
"""

import json
from .base import BaseAgent


scoring_agent = BaseAgent(
    name="ScoringAgent",
    system_prompt="""
You are an expert technical recruiter specialised in the Kenyan tech job market.

You will receive:
1. Structured CV data (JSON)
2. A job description

Score the candidate from 0–100 across 4 dimensions.
Consider Kenyan-specific context:
  - University of Nairobi, Strathmore, JKUAT, KCA are strong local universities
  - Safaricom, KCB, Equity Bank, Andela are prestigious employers
  - M-Pesa/mobile money experience is highly valued for fintech roles
  - KCSE grade A- (78 points) or above indicates top 15% of students

Return ONLY valid JSON with these exact keys:
  overall_score (integer 0-100)
  recommendation (string: "hire", "maybe", or "reject")
  breakdown (object with: technical_skills, experience, education, culture_fit)
  Each breakdown item must have: score (integer), reasoning (string, min 20 words)

Return ONLY the raw JSON. No markdown. No explanation outside the JSON. No code fences.
"""
)

score_checker = BaseAgent(
    name="ScoreChecker",
    system_prompt="""
You are a quality checker for candidate scoring outputs.

You will receive a JSON scoring result. Verify:
1. It is valid JSON
2. 'overall_score' is an integer between 0 and 100
3. 'recommendation' is one of: "hire", "maybe", "reject"
4. 'breakdown' has all 4 keys: technical_skills, experience, education, culture_fit
5. Each breakdown item has a 'reasoning' with at least 20 words
6. The overall_score roughly matches the breakdown scores (not wildly inconsistent)

If ALL checks pass: respond with exactly: ok
If ANY fail: respond with: retry
Then list which checks failed.
"""
)


def score_candidate(cv_data: dict, jd_text: str) -> dict:
    """Score a candidate CV against a job description."""
    prompt = f"""
JOB DESCRIPTION:
{jd_text}

CANDIDATE CV DATA:
{json.dumps(cv_data, indent=2)}

Score this candidate for the job.
"""
    raw = scoring_agent.run_with_retry(
        user_input=prompt,
        checker=score_checker,
        max_retries=3
    )

    clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(clean)
