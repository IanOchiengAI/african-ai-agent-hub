# 🌍 African AI Agent Hub

The AI revolution shouldn't be imported — it should be built locally.

Welcome to the **African AI Agent Hub**, an open-source initiative and public build log documenting a 6-month journey to build production-grade AI agents tailored specifically for African workflows and use cases.

**Build log:** Sprint 1 is live — building in public because nothing ever goes wrong.

---

## 🎯 The Mission

To build specialized, robust AI agents that solve real problems on the ground in Africa. Instead of generic wrappers, these agents are designed with deep local context — understanding informal markets, local payment gateways (M-Pesa), and vernacular languages (Swahili).

---

## 🚀 The Three Agents

### 1. 🇰🇪 Kenyan Hiring Agent ← *Current Sprint*
A CV screening and candidate matching agent built with deep Kenyan job market context. It understands the nuances between the CBC and 8-4-4 education systems, interprets informal experience, and maps local unstructured data to structured employer requirements.

**Status:** Sprint 1 — Active  
**Folder:** `agent-1-kenyan-hiring/`

### 2. 💳 M-Pesa SME Accounting Agent
A business automation agent that runs in the background for Kenyan SMEs. It ingests raw M-Pesa transaction statements, categorizes income and expenses, flags anomalies, and generates simple profit/loss summaries — all without requiring formal accounting knowledge from the business owner.

**Status:** Not started (Sprint 2)  
**Folder:** `agent-2-mpesa-accounting/`

### 3. 🌱 Crop Doctor
A Swahili-first WhatsApp agent designed for smallholder farmers. It accepts photos of crops, diagnoses diseases using multimodal vision models, and provides actionable agronomy and weather advice via an accessible messaging interface.

**Status:** Not started (Sprint 3)  
**Folder:** `agent-3-crop-doctor/`

---

## 📁 Repo Structure

```
african-ai-agent-hub/
├── README.md                    ← This file
├── Sprint-1-Tracker.md          ← Live sprint progress
├── 03-Resources-Library.md      ← Learning resources
├── Projects/
│   ├── Project-1-Kenyan-Hiring-Agent.md
│   ├── Project-2-Crop-Doctor.md
│   └── Project-3-MPesa-SME-Accounting-Agent.md
└── Milestones/
    ├── Phase-1-Foundation.md
    └── Phase-2-3-4-Outlines.md
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **LLM:** Anthropic Claude (claude-sonnet-4-5)
- **Package manager:** `uv`
- **SMS (later):** Africa's Talking
- **Document parsing:** pypdf2, python-docx

---

## 📅 Timeline

| Sprint | Weeks | Agent | Target Date |
|--------|-------|-------|------------|
| Sprint 1 | 1–8 | Kenyan Hiring Agent | September 21, 2026 |
| Sprint 2 | 9–16 | M-Pesa SME Accounting Agent | November 2026 |
| Sprint 3 | 17–24 | Crop Doctor | January 2027 |

---

## 🤝 Building in Public

This is a learning-by-building project. Every sprint produces working code, a demo, and a write-up of what I learned. Follow the journey on LinkedIn and GitHub.
