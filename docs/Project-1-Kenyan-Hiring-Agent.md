# Project 1: Kenyan Hiring Agent

**Sprint:** 1 (Weeks 1–8) — **Current Build**  
**Complexity:** Medium  
**Target Users:** Kenyan HR departments, recruitment agencies, SMEs  
**Target Completion:** September 21, 2026

---

## Problem Statement

Kenyan employers struggle with CV screening because:
- CVs mix education systems (8-4-4 vs CBC vs international)
- Informal work experience is not standardized
- Skills are listed inconsistently
- Manual screening is slow and biased
- No locally-aware CV screening tools exist

---

## Solution: AI-Powered CV Screening Agent

An agent that:
1. Understands Kenyan education context (8-4-4, CBC, international, polytechnics)
2. Extracts structured data from messy, inconsistently formatted CVs
3. Scores candidates against job requirements (0–100)
4. Generates contextual interview questions based on CV gaps
5. Produces ranked shortlist recommendations

---

## Sprint 1 Build Checklist

- [ ] Week 1: First Anthropic API call working locally
- [ ] Week 2: CV extraction prompt — extracts name, education system, experience, skills from plain text
- [ ] Week 3: Tool calling — `extract_education()`, `extract_experience()`, `extract_skills()`
- [ ] Week 4: Matching engine — `calculate_fit_score()` against a job description
- [ ] Week 5: Batch processing — handle 10 CVs in one run
- [ ] Week 6: File support — accept PDF and DOCX inputs
- [ ] Week 7: Interview question generator — `generate_questions()` based on CV gaps
- [ ] Week 8: v0.1 demo — end-to-end run, push to GitHub, write build log

---

## Technical Architecture

### Core Components

**1. Document Processor**
- Input: PDF / DOCX / TXT CVs
- Extract text using `pypdf2`, `python-docx`, `mammoth`
- Clean formatting, handle Swahili/English mix
- Output: Clean plain text

**2. Data Extraction Agent**
```python
Tools:
- extract_personal_info()     # Name, email, phone, location
- extract_education()         # Understands 8-4-4, CBC, international
- extract_experience()        # Handles informal work, gaps, side hustles
- extract_skills()            # Tech and soft skills
- extract_certifications()    # Formal and informal certs
```

**3. Matching Engine**
```python
Tools:
- compare_skills(cv_skills, job_requirements)
- score_experience(cv_experience, job_level)
- evaluate_education(cv_education, job_education_req)
- calculate_fit_score()       # Returns 0–100
```

**4. Interview Question Generator**
```python
Tool:
- generate_questions(cv_data, job_role)
  # Returns 5–7 role-specific questions based on CV gaps
```

**5. Output Generator**
- Structured JSON report
- Human-readable text summary
- (Later) PDF shortlist summary
- (Later) SMS notification to candidates via Africa's Talking

---

## Key Features

### Kenyan Context Understanding

**Education Systems:**
| System | Levels | Notes |
|--------|--------|-------|
| 8-4-4 | KCPE → KCSE → University | Still most common on CVs |
| CBC | Junior → Senior → KPSEA | Newer system, less common on CVs yet |
| International | IGCSE, IB, A-Levels | Private school candidates |
| Informal | Polytechnics, bootcamps, apprenticeships | Often undervalued — agent corrects for this |

**Experience Patterns the Agent Understands:**
- "Informal sector" experience (jua kali, market traders)
- "Hustles" and side projects as real work experience
- Employment gaps (common — school fees, family obligations)
- Internships and volunteer work counted appropriately
- "Freelance" and contract roles listed without end dates

**Skills Recognition:**
- Local tech stack (PHP, WordPress still dominant in SMEs)
- Mobile money integration (M-Pesa, Airtel Money)
- Multi-language requirements (English + Swahili)
- ERP systems common in Nairobi corporates (SAP, Sage)

### Intelligence Features

1. **Contextual Scoring** — not just keyword matching; understands role progression
2. **Bias Detection** — flags gender-biased language in job descriptions; removes university name bias; focuses on skills/experience
3. **Gap Analysis** — identifies missing skills; suggests training resources; generates development questions

---

## User Flow

```
1. HR uploads job description + candidate CVs (batch)
2. Agent processes each CV:
   - Extracts structured data
   - Scores against job requirements
   - Generates interview questions
3. Agent outputs:
   - Ranked shortlist (top 10 candidates)
   - Detailed scorecards per candidate
   - Interview question sets per candidate
   - (Optional) Rejection email drafts
4. HR reviews and approves shortlist
5. (Later) SMS notifications sent to shortlisted candidates via Africa's Talking
```

---

## Data Schema

### CV Data Structure
```json
{
  "personal": {
    "name": "John Kamau",
    "email": "john@example.com",
    "phone": "+254712345678",
    "location": "Nairobi"
  },
  "education": [
    {
      "level": "University",
      "institution": "University of Nairobi",
      "degree": "BSc Computer Science",
      "system": "8-4-4",
      "graduation_year": 2020,
      "grade": "Second Class Upper"
    },
    {
      "level": "Secondary",
      "institution": "Alliance High School",
      "system": "8-4-4",
      "graduation_year": 2016,
      "grade": "B+ (70 points)"
    }
  ],
  "experience": [
    {
      "title": "Software Developer",
      "company": "Safaricom PLC",
      "start": "2021-03",
      "end": "present",
      "type": "formal",
      "description": "Built M-Pesa integrations..."
    },
    {
      "title": "Freelance Web Developer",
      "company": "Self-employed",
      "start": "2020-06",
      "end": "2021-02",
      "type": "informal",
      "description": "WordPress sites for SMEs in Westlands"
    }
  ],
  "skills": {
    "technical": ["Python", "PHP", "WordPress", "M-Pesa API", "MySQL"],
    "soft": ["Communication", "Team leadership"],
    "languages": ["English", "Swahili"]
  },
  "certifications": [
    {
      "name": "Google IT Support Certificate",
      "issuer": "Google / Coursera",
      "year": 2022
    }
  ]
}
```

### Job Requirement Structure
```json
{
  "title": "Junior Software Developer",
  "company": "Nairobi Fintech Ltd",
  "required_skills": ["Python", "REST APIs", "SQL"],
  "preferred_skills": ["M-Pesa API", "FastAPI"],
  "min_experience_years": 1,
  "education_requirement": "Degree or equivalent",
  "education_systems_accepted": ["8-4-4", "CBC", "International", "Informal"],
  "location": "Nairobi (hybrid)"
}
```

### Scorecard Output Structure
```json
{
  "candidate_name": "John Kamau",
  "job_title": "Junior Software Developer",
  "fit_score": 82,
  "recommendation": "SHORTLIST",
  "skill_match": {
    "matched": ["Python", "REST APIs", "SQL", "M-Pesa API"],
    "missing": [],
    "bonus": ["WordPress", "MySQL"]
  },
  "experience_score": 85,
  "education_score": 90,
  "interview_questions": [
    "Your CV shows freelance WordPress work — can you describe a project where you had to integrate a payment system?",
    "You transitioned from freelance to Safaricom in 2021. What drove that decision and what did you learn?"
  ],
  "notes": "Strong M-Pesa API experience is a significant plus for this role."
}
```

---

## Sprint 1 File Structure

```
agent-1-kenyan-hiring/
├── README.md
├── pyproject.toml            ← Dependencies
├── .env.example              ← API key template
├── src/
│   ├── __init__.py
│   ├── agent.py              ← Main agent loop
│   ├── extractor.py          ← CV data extraction tools
│   ├── matcher.py            ← Scoring and matching engine
│   ├── question_gen.py       ← Interview question generator
│   └── document_processor.py ← PDF/DOCX → text
├── prompts/
│   ├── system_prompt.md      ← Main system prompt
│   ├── extraction_prompt.md
│   └── scoring_prompt.md
├── data/
│   ├── sample_cvs/           ← Test CVs (anonymized)
│   └── sample_job_descriptions/
└── tests/
    ├── test_extractor.py
    └── test_matcher.py
```
