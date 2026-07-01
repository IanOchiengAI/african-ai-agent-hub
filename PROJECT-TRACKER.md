# 🌍 African AI Agent Hub — Project Tracker

> **Build period:** June 2026 – December 2026 (24 weeks)  
> **GitHub:** https://github.com/IanOchiengAI/african-ai-agent-hub  
> **Status:** Sprint 1 — Active 🟢

---

## The Three Agents

| # | Agent | Status | Sprint | Notes |
|---|-------|--------|--------|-------|
| 1 | 🇰🇪 Kenyan Hiring Agent | 🟡 Building | Sprint 1 (Wks 1–8) | **Current focus** |
| 2 | 💳 M-Pesa SME Accounting Agent | ⬜ Not started | Sprint 2 (Wks 9–16) | — |
| 3 | 🌱 Crop Doctor | ⬜ Not started | Sprint 3 (Wks 17–24) | — |

---

## Sprint 1 — Kenyan Hiring Agent (Weeks 1–8)

> Target completion: **~21 September 2026**

### Phase Checklist

- [x] Repo created and pushed to GitHub
- [x] Project documentation written (README, all 3 project specs, milestones)
- [x] LinkedIn announcement posted
- [ ] Local development environment set up (Python, venv, API keys)
- [ ] `agent-1-kenyan-hiring/` folder initialised with `pyproject.toml`
- [ ] Week 1: First successful Anthropic API call from local machine
- [ ] Week 2: CV text extraction prompt working (plain text CVs)
- [ ] Week 3: Tool calling implemented (extract_education, extract_experience, extract_skills)
- [ ] Week 4: Matching engine — score a CV against a job description (0–100)
- [ ] Week 5: Batch processing — handle 10 CVs at once
- [ ] Week 6: PDF/DOCX input support added
- [ ] Week 7: Interview question generator added
- [ ] Week 8: v0.1 — end-to-end demo working, pushed to GitHub

### Build Log (update as you go)

| Week | Date | What I built | What I learned | Blockers |
|------|------|-------------|----------------|---------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

---

## Sprint 2 — M-Pesa SME Accounting Agent (Weeks 9–16)

> Status: Not started. Planning begins after Sprint 1 demo.

---

## Sprint 3 — Crop Doctor (Weeks 17–24)

> Status: Not started. Planning begins after Sprint 2 demo.

---

## Key Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| June 2026 | Build order: Hiring → M-Pesa → Crop Doctor | Complexity order: easiest to hardest |
| June 2026 | Leading with Kenyan Hiring Agent in Sprint 1 | Text-in/text-out = fewest moving parts |
| June 2026 | Using Anthropic Claude API as primary LLM | Tool use is best-in-class; aligns with learning goals |

---

## Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| Language | Python 3.12+ | Industry standard for AI/ML |
| LLM | Anthropic Claude (claude-sonnet) | Best tool calling, structured output |
| Package manager | `uv` | Fast, modern replacement for pip |
| SMS (later) | Africa's Talking | Kenyan-native, M-Pesa friendly |
| PDF parsing | `pypdf2` + `python-docx` | Handle CV file formats |
| Testing | `pytest` | Standard Python testing |

---

## Resources

- Anthropic Docs: https://docs.anthropic.com
- Africa's Talking: https://africastalking.com/docs
- CS50P (Python): https://cs50.harvard.edu/python/2022/
- Prompt Engineering Guide: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
