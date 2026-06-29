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
| **Week 1** | Python environment + first API call | 🟡 In Progress | `uv` setup, `.env` config, first Claude call |
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
**Goal:** Claude can extract structured fields from a plain-text CV

**Deliverables:**
- [ ] System prompt written for a Kenyan CV screener
- [ ] Script extracts: name, education system, experience years, top 5 skills
- [ ] Tested on 5 different sample CVs
- [ ] Results saved as JSON

---

### Week 3 — Tool Calling: Structured Extraction
**Goal:** Replace single-prompt extraction with proper tool calling

**Deliverables:**
- [ ] `extract_education()` tool defined and working
- [ ] `extract_experience()` tool working (handles informal/gap/freelance)
- [ ] `extract_skills()` tool working
- [ ] All tools return clean JSON with error handling

---

### Week 4 — Matching Engine: Fit Scoring
**Goal:** Given a structured CV and a job description, produce a 0–100 fit score

**Deliverables:**
- [ ] `compare_skills()`, `score_experience()`, `evaluate_education()` tools
- [ ] `calculate_fit_score()` — combines all signals into one number
- [ ] Tested on 5 CV + job description pairs

---

### Week 5 — Batch Processing
**Goal:** Process 10 CVs against one job description in a single run

**Deliverables:**
- [ ] Loop over a folder of CVs, output ranked list
- [ ] Total run time < 2 minutes for 10 CVs

---

### Week 6 — File Support: PDF & DOCX
**Goal:** Agent accepts real CV files, not just copy-pasted text

**Deliverables:**
- [ ] `pypdf2` and `python-docx` integration
- [ ] Handle encoding errors and formatting noise

---

### Week 7 — Interview Question Generator
**Goal:** For each shortlisted candidate, generate 5–7 tailored interview questions

**Deliverables:**
- [ ] `generate_questions(cv_data, job_role)` tool
- [ ] Questions reference specific CV content and probe skill gaps

---

### Week 8 — v0.1 Demo & Sprint Review
**Goal:** End-to-end working demo. Push everything. Write the Sprint 1 post.

**Deliverables:**
- [ ] Full pipeline: PDF/DOCX CVs → structured data → scores → shortlist → questions
- [ ] Clean README in `agent-1-kenyan-hiring/` with setup instructions
- [ ] All code pushed to GitHub
- [ ] Sprint 1 LinkedIn post / Substack write-up published

---

## What Sprint 1 Does NOT Include

To keep scope tight, the following are deferred:

- ❌ Web UI or frontend (command-line only for now)
- ❌ SMS notifications via Africa's Talking (Sprint 2)
- ❌ PDF output / formatted reports (Sprint 2)
- ❌ Database or persistent storage (Sprint 2)
- ❌ Deployment / hosting (Sprint 3)
