# Project 1: Kenyan Hiring Agent

**Timeline**: Weeks 17-18 (Phase 4)  
**Complexity**: Medium  
**Target Users**: Kenyan HR departments, recruitment agencies

---

## Problem Statement

Kenyan employers struggle with CV screening because:
- CVs mix education systems (8-4-4 vs CBC vs international)
- Informal work experience not standardized
- Skills listed inconsistently
- Manual screening is slow and biased
- No local CV screening tools exist

---

## Solution: AI-Powered CV Screening Agent

An agent that:
1. Understands Kenyan education context
2. Extracts structured data from messy CVs
3. Scores candidates against job requirements
4. Generates contextual interview questions
5. Produces shortlist recommendations

---

## Technical Architecture

### Core Components

**1. Document Processor**
- Input: PDF/DOCX/TXT CVs
- Extract text (pypdf2, python-docx, mammoth)
- Clean formatting, handle Swahili/English mix
- Output: Clean text

**2. Data Extraction Agent**
```python
Tools:
- extract_personal_info()
- extract_education() # Understands 8-4-4, CBC, international
- extract_experience() # Handles informal work, gaps
- extract_skills()
- extract_certifications()
```

**3. Matching Engine**
```python
Tools:
- compare_skills(cv_skills, job_requirements)
- score_experience(cv_experience, job_level)
- evaluate_education(cv_education, job_education_req)
- calculate_fit_score() # Returns 0-100
```

**4. Interview Question Generator**
```python
Tool:
- generate_questions(cv_data, job_role)
# Returns 5-7 role-specific questions based on CV gaps
```

**5. Output Generator**
- Structured JSON report
- PDF shortlist summary
- SMS notification to candidates (Africa's Talking)

---

## Key Features

### Kenyan Context Understanding

**Education Systems**:
- 8-4-4: KCPE → KCSE → University/College
- CBC: Junior School → Senior School → KPSEA
- International: IGCSE, IB, A-Levels
- Informal: Polytechnics, bootcamps, apprenticeships

**Experience Patterns**:
- Recognize "informal sector" experience
- Value "hustles" and side projects
- Understand employment gaps (common in Kenya)
- Count internships and volunteer work

**Skills Recognition**:
- Local tech stack (PHP, WordPress still dominant)
- Mobile money integration (M-Pesa, Airtel Money)
- Multi-language requirements (English/Swahili)

### Intelligence Features

1. **Contextual Scoring**:
   - Not just keyword matching
   - Understands role progression
   - Values transferable skills

2. **Bias Detection**:
   - Flags gender-biased language in job description
   - Removes university name bias
   - Focuses on skills/experience

3. **Gap Analysis**:
   - Identifies missing skills
   - Suggests training resources
   - Generates development questions

---

## User Flow

```
1. HR uploads job description + candidate CVs (batch)
2. Agent processes each CV:
   - Extracts structured data
   - Scores against job requirements
   - Generates interview questions
3. Agent outputs:
   - Ranked shortlist (top 10)
   - Detailed scorecards per candidate
   - Interview question sets
   - Rejection emails (optional)
4. HR reviews and approves
5. SMS notifications sent to shortlisted candidates
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
    }
  ],
  "experience": [
    {
      "title": "Software Developer",
      "company": "Safaricom",
      "duration_months": 24,
      "type": "formal",
      "responsibilities": ["Built M-Pesa integrations", "..."]
    },
    {
      "title": "Freelance Web Developer",
      "type": "informal",
      "duration_months": 12,
      "projects": ["E-commerce sites", "WordPress"]
    }
  ],
  "skills": {
    "technical": ["Python", "Django", "JavaScript", "M-Pesa API"],
    "languages": ["English (native)", "Swahili (fluent)"],
    "soft": ["Team leadership", "Communication"]
  },
  "certifications": ["AWS Certified", "Google Analytics"],
  "portfolio": ["github.com/...", "website.com"]
}
```

### Scoring Output
```json
{
  "candidate": "John Kamau",
  "overall_score": 78,
  "breakdown": {
    "education_match": 90,
    "experience_match": 75,
    "skills_match": 70,
    "cultural_fit": 80
  },
  "strengths": [
    "Strong M-Pesa integration experience",
    "Bilingual",
    "Local market knowledge"
  ],
  "concerns": [
    "No cloud deployment experience",
    "Short tenure at previous role"
  ],
  "recommendation": "Interview",
  "interview_questions": [
    "Describe a complex M-Pesa integration challenge you solved",
    "How do you handle deployment in production environments?",
    "..."
  ]
}
```

---

## Implementation Roadmap

### Week 17: Core Agent
- [ ] Set up project structure
- [ ] Build document processor
- [ ] Create extraction agent with tools
- [ ] Test on 20 real Kenyan CVs
- [ ] Build matching engine
- [ ] Implement scoring algorithm

### Week 18: Interface & Deployment
- [ ] Build web interface (Streamlit/Gradio)
- [ ] Add batch upload
- [ ] Integrate Africa's Talking SMS
- [ ] Create PDF report generator
- [ ] Deploy to Vercel/Replit
- [ ] Write documentation

---

## Testing Strategy

### Test Data
- Collect 50 anonymized Kenyan CVs:
  - 20 tech roles
  - 15 business roles
  - 15 mixed backgrounds
- Mix of 8-4-4, CBC, international education
- Various experience levels

### Validation
- Compare agent scores vs human recruiter scores
- Target: >80% agreement on top 10 candidates
- Measure: processing time (should be <10 seconds/CV)

---

## Success Metrics

**Technical**:
- [ ] Process 100 CVs in <15 minutes
- [ ] Accuracy >85% on data extraction
- [ ] Zero API failures with retry logic
- [ ] Cost <$0.10 per CV processed

**Product**:
- [ ] Deployed and accessible online
- [ ] 5+ Kenyan recruiters test it
- [ ] Feedback collected
- [ ] Demo video published

**Content**:
- [ ] Before AGI article: "Building AI for Kenya: Hiring Agent Case Study"
- [ ] Technical deep-dive on blog
- [ ] GitHub repo with documentation

---

## Monetization Potential

**Pricing Model**:
- Free: 10 CVs/month
- Starter: $29/month - 100 CVs
- Pro: $99/month - 500 CVs
- Enterprise: Custom

**Target Market**:
- Kenyan recruitment agencies (50+ in Nairobi)
- HR departments (banks, telcos, tech companies)
- Staffing firms

**Revenue Goal**: First paying customer by Week 24

---

## Tech Stack

- **Backend**: Python + FastAPI
- **Agent**: Anthropic Claude (Haiku for cost)
- **Document Processing**: pypdf2, mammoth, python-docx
- **SMS**: Africa's Talking API
- **Database**: SQLite → PostgreSQL later
- **Frontend**: Streamlit (simple) or Next.js (advanced)
- **Deployment**: Vercel/Railway
- **Monitoring**: Helicone

---

## Code Structure

```
kenyan-hiring-agent/
├── src/
│   ├── agents/
│   │   ├── extractor.py
│   │   ├── matcher.py
│   │   └── interviewer.py
│   ├── tools/
│   │   ├── document_processor.py
│   │   ├── education_analyzer.py
│   │   └── sms_sender.py
│   ├── utils/
│   │   ├── prompts.py
│   │   └── schemas.py
│   └── app.py
├── tests/
├── data/
│   ├── sample_cvs/
│   └── job_descriptions/
├── docs/
└── README.md
```

---

## Next Steps

1. Start Week 17 after completing Phase 3
2. Collect test CVs during Phase 1-2
3. Draft prompts during Phase 2
4. Build prototype during Week 17-18

---

**Related Projects**:
- [[Project-2-Agricultural-Extension-Agent]]
- [[Project-3-MPesa-Workflow-Agent]]

**Prerequisites**:
- Complete [[Phase-1-Foundation]]
- Complete [[Phase-2-Frameworks]]
- Complete [[Phase-3-Production]]
