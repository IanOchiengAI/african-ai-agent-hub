"""
cv_extractor.py — CVExtractorAgent + ExtractorChecker
=======================================================
Sub-Agent 1: Extract structured data from a raw CV.

Output format (JSON):
{
  "name": "John Kamau Mwangi",
  "email": "john.kamau@gmail.com",
  "location": "Nairobi, Kenya",
  "education": [
    {"degree": "BSc Computer Science", "institution": "University of Nairobi", "year": "2020", "grade": "Second Class Upper"}
  ],
  "experience": [
    {"title": "Software Developer", "company": "Safaricom PLC", "duration": "March 2021–Present", "highlights": ["..."]}
  ],
  "skills": {
    "technical": ["Python", "Django", "M-Pesa Daraja API"],
    "soft": ["Communication", "Teamwork"],
    "languages": ["English", "Swahili"]
  },
  "certifications": ["Google IT Support Professional Certificate"]
}
"""

import json
from .base import BaseAgent


# ── The extractor agent ───────────────────────────────────────────────────────
cv_extractor = BaseAgent(
    name="CVExtractorAgent",
    system_prompt="""
You are a CV parser specialised in East African job markets.

Given raw CV text, extract ALL information and return it as valid JSON.
The JSON must have exactly these top-level keys:
  - name (string)
  - email (string)
  - location (string)
  - education (list of objects with: degree, institution, year, grade)
  - experience (list of objects with: title, company, duration, highlights)
  - skills (object with: technical, soft, languages — each a list of strings)
  - certifications (list of strings)

Return ONLY the raw JSON. No markdown. No explanation. No code fences.
If a field is missing from the CV, use an empty string or empty list.
"""
)

# ── The checker agent (the LoopAgent's validator) ─────────────────────────────
extractor_checker = BaseAgent(
    name="ExtractorChecker",
    system_prompt="""
You are a JSON validator for CV extractions.

You will receive a JSON string. Check that:
1. It is valid JSON (parseable)
2. It has all required keys: name, email, location, education, experience, skills, certifications
3. 'name' is a non-empty string
4. 'experience' is a non-empty list (CVs must have at least one job)
5. 'skills' has a 'technical' key with at least one item

If ALL checks pass, respond with exactly: ok
If ANY check fails, respond with: retry
Then list exactly which checks failed and why.
"""
)


def extract_cv(cv_text: str) -> dict:
    """
    Run CVExtractorAgent with the LoopAgent retry pattern.
    Returns a parsed dict of the CV data.
    """
    raw = cv_extractor.run_with_retry(
        user_input=f"Extract all information from this CV:\n\n{cv_text}",
        checker=extractor_checker,
        max_retries=3
    )

    # Parse JSON — strip any accidental markdown fences
    clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(clean)
