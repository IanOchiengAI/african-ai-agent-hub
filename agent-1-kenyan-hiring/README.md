# 🇰🇪 Agent 1: Kenyan Hiring Agent

**Sprint 1 — Active build** | Powered by **Gemini 3.5 Flash** (High Thinking)

This is a multi-agent CV screening and candidate evaluation pipeline tailored specifically for the Kenyan tech job market. It extracts details from raw CVs, evaluates them against a Job Description using local East African context, and outputs a structured hire/no-hire recommendation.

---

## 📐 Architecture & Multi-Agent Flow

The system runs a sequential pipeline using Google's ReAct and validation loop patterns:

1. **`CVExtractorAgent` (Stage 1)**: Reads raw text from a CV and outputs structured JSON (name, education, experience, skills, certifications).
   - *Validation:* `ExtractorChecker` verifies that the JSON is parseable, non-empty, and has at least one job experience. If validation fails, it retries (up to 3 times).
2. **`ScoringAgent` (Stage 2)**: Compares structured CV data against a Job Description, scoring 0-100 across Technical Skills, Experience, Education, and Culture Fit.
   - *Validation:* `ScoreChecker` verifies the scores and reasons. If it fails, it retries (up to 3 times).
3. **`ReportAgent` (Stage 3)**: Formats a polished natural language memo with key strengths, concerns, and recommended interview questions.

---

## ⚡ Quick Start

### 1. Install Dependencies
Make sure you have [uv](https://github.com/astral-sh/uv) installed:
```bash
uv sync
```

### 2. Configure your API Key
Copy the `.env.example` template:
```bash
copy .env.example .env
```
Open the `.env` file and replace the placeholder with your **Gemini API key** from Google AI Studio:
```
GOOGLE_API_KEY=AIzaSy...
```

### 3. Run the Agent
To analyze a single CV against a job description, run:
```bash
uv run python src/agent.py \
  --cv data/sample_cvs/sample_1_john_kamau.txt \
  --job data/sample_job_descriptions/junior_dev.txt
```

---

## 🌐 Run the Streamlit Web Application (Local)
To launch the user-friendly web interface locally:
```bash
uv run streamlit run streamlit_app.py
```
This runs the web server locally, letting you paste CVs and Job Descriptions to generate PDF-exportable recommendations.
