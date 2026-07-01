# 🌍 African AI Agent Hub — Sprint 1 Build Log

> **Sprint 1 Status: ACTIVE** 🟢  
> **Repo:** [IanOchiengAI/african-ai-agent-hub](https://github.com/IanOchiengAI/african-ai-agent-hub)  
> **Target Completion:** September 21, 2026  
> **Agent:** Kenyan Hiring Agent (Agent 1 of 3)

---

## Sprint 1 Goal

Build a working v0.1 of the Kenyan Hiring Agent — an AI tool that takes a job description and a batch of CVs, and produces a ranked shortlist with scorecards and interview questions.

By end of Sprint 1, it should be able to process plain-text and PDF CVs and output a usable shortlist. No UI. No deployment. Just working Python code.

---

## 🗓️ Engineering Roadmap

| Phase | Focus Area | Status | Technical Details |
|-------|------------|--------|-------------------|
| **Environment** | Infrastructure setup & repo launch | ✅ Done | Monorepo created, docs pushed to GitHub |
| **Week 1** | Python environment + first API call | ⬜ Upcoming | `uv` setup, `.env` config, first Claude call |
| **Week 2** | Prompt engineering — CV extraction | ⬜ Upcoming | Extract name, education system, experience from plain text |
| **Week 3** | Tool calling — structured extraction | ⬜ Upcoming | `extract_education()`, `extract_experience()`, `extract_skills()` |
| **Week 4** | Matching engine — fit scoring | ⬜ Upcoming | `calculate_fit_score()`, 0–100 scoring against job description |
| **Week 5** | Batch processing | ⬜ Upcoming | Handle 10 CVs in a single run |
| **Week 6** | File support | ⬜ Upcoming | PDF and DOCX input via `pypdf2` and `python-docx` |
| **Week 7** | Interview question generator | ⬜ Upcoming | `generate_questions()` based on CV gaps |
| **Week 8** | v0.1 demo + build log | ⬜ Upcoming | End-to-end run, push to GitHub, write Sprint 1 post |

---

## Week-by-Week Build Log

### Week 1 — Environment Setup & First API Call
**Goal:** Python working locally, first successful Claude API call

**Deliverables:**
- [ ] `uv` installed, virtual environment created
- [ ] `.env` file configured with `ANTHROPIC_API_KEY`
- [ ] `hello_claude.py` — script that sends a question and prints the response
- [ ] Folder `agent-1-kenyan-hiring/` initialised with `pyproject.toml`

---

### Week 2 — Prompt Engineering: CV Extraction
**Goal:** Claude can extract structured fields from a plain-text CV using a well-crafted prompt

**Deliverables:**
- [ ] System prompt written for a Kenyan CV screener
- [ ] Script extracts: name, education system (8-4-4/CBC/international), experience years, top 5 skills
- [ ] Tested on 5 different sample CVs (different formats, different education systems)
- [ ] Results saved as JSON

---

### Week 3 — Tool Calling: Structured Extraction
**Goal:** Replace single-prompt extraction with proper tool calling for each CV section

**Deliverables:**
- [ ] `extract_education()` tool defined and working
- [ ] `extract_experience()` tool working (handles informal/gap/freelance)
- [ ] `extract_skills()` tool working
- [ ] All tools return clean JSON
- [ ] Error handling in place

---

### Week 4 — Matching Engine: Fit Scoring
**Goal:** Given a structured CV and a job description, produce a 0–100 fit score

**Deliverables:**
- [ ] `compare_skills()` tool — matches CV skills to job requirements
- [ ] `score_experience()` tool — evaluates years and relevance
- [ ] `evaluate_education()` tool — no bias toward specific institutions
- [ ] `calculate_fit_score()` — combines all signals into one number
- [ ] Tested on 5 CV + job description pairs

---

### Week 5 — Batch Processing
**Goal:** Process 10 CVs against one job description in a single run

**Deliverables:**
- [ ] Loop over a folder of CVs
- [ ] Process each and collect scorecards
- [ ] Output a ranked list (highest fit score first)
- [ ] Total run time < 2 minutes for 10 CVs

---

### Week 6 — File Support: PDF & DOCX
**Goal:** Agent accepts real CV files, not just copy-pasted text

**Deliverables:**
- [ ] `pypdf2` integration — extract text from PDF CVs
- [ ] `python-docx` integration — extract text from DOCX CVs
- [ ] Handle encoding errors and formatting noise
- [ ] Tested on 5 real CV files (anonymized)

---

### Week 7 — Interview Question Generator
**Goal:** For each shortlisted candidate, generate 5–7 tailored interview questions

**Deliverables:**
- [ ] `generate_questions(cv_data, job_role)` tool working
- [ ] Questions reference specific CV content (not generic)
- [ ] Questions probe identified skill gaps
- [ ] Output appended to candidate scorecard

---

### Week 8 — v0.1 Demo & Sprint Review
**Goal:** End-to-end working demo. Push everything. Write the Sprint 1 post.

**Deliverables:**
- [ ] Full pipeline working: PDF/DOCX CVs → structured data → scores → shortlist → questions
- [ ] Clean `README.md` in `agent-1-kenyan-hiring/` with setup instructions
- [ ] All code pushed to GitHub
- [ ] Sprint 1 LinkedIn post / Substack write-up published
- [ ] Sprint 2 planning begun

---

## What Sprint 1 Does NOT Include

To keep scope tight, the following are deferred to later:

- ❌ Web UI or frontend (command-line only for now)
- ❌ SMS notifications via Africa's Talking (Sprint 2)
- ❌ PDF output / formatted reports (Sprint 2)
- ❌ Database or persistent storage (Sprint 2)
- ❌ Deployment / hosting (Sprint 3)
