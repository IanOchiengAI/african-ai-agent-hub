import streamlit as st
import time
import os
import json
import collections
from pathlib import Path
from PyPDF2 import PdfReader
import docx

# Configure Page
st.set_page_config(
    page_title="Kenyan Hiring Agent — CV Screener",
    page_icon="🇰🇪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Styling / Themes
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 700;
        color: #008751; /* Kenyan Green */
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666666;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #008751 !important;
        color: white !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        width: 100% !important;
        padding: 0.6rem 0 !important;
    }
    .report-box {
        background-color: #F4F6F5;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 5px solid #008751;
        font-family: inherit;
    }
</style>
""", unsafe_allow_html=True)

# ── Load environment / API key ────────────────────────────────────────────────
# Check Streamlit secrets first (for cloud deployment), then local environment
GOOGLE_API_KEY = None
if "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    from dotenv import load_dotenv
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set the key in environmental variables so the sub-agents can read it
if GOOGLE_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    os.environ["GEMINI_API_KEY"] = GOOGLE_API_KEY

# Import sub-agents after setting environmental variables
try:
    import sys
    sys.path.insert(0, str(Path(__file__).parent / "src"))
    from agents.cv_extractor import extract_cv
    from agents.scorer import score_candidate
    from agents.reporter import generate_report
except Exception as e:
    st.error(f"Failed to import agent modules: {e}")
    st.stop()

# ── Rate Limiting Setup (Process-wide memory) ─────────────────────────────────
RATE_LIMIT_COOLDOWN = 60  # seconds between runs per user/IP
DAILY_MAX_RUNS = 100      # maximum runs overall per day
MAX_CHARS = 6000          # character limit for input safety

if not hasattr(st, "_global_rate_limits"):
    st._global_rate_limits = {}
if not hasattr(st, "_global_daily_runs"):
    st._global_daily_runs = []

def get_client_ip() -> str:
    """Retrieve client IP address from request headers or fallback to session UUID."""
    try:
        headers = st.context.headers
        ip = headers.get("x-forwarded-for") or headers.get("forwarded") or headers.get("host")
        if ip:
            return ip.split(",")[0].strip()
    except Exception:
        pass
    
    if "session_ip_fallback" not in st.session_state:
        import uuid
        st.session_state.session_ip_fallback = str(uuid.uuid4())
    return st.session_state.session_ip_fallback

def check_rate_limits(client_ip: str) -> tuple[bool, str]:
    """Check if the user or global app limits have been hit."""
    now = time.time()
    
    # Clean up daily logs older than 24 hours
    cutoff = now - 86400
    st._global_daily_runs = [t for t in st._global_daily_runs if t > cutoff]
    
    # Check global day limit
    if len(st._global_daily_runs) >= DAILY_MAX_RUNS:
        return False, "The app has reached its global daily demonstration limit. Please try again tomorrow."
        
    # Check IP cooldown limit
    if client_ip in st._global_rate_limits:
        last_run = st._global_rate_limits[client_ip]
        elapsed = now - last_run
        if elapsed < RATE_LIMIT_COOLDOWN:
            remaining = int(RATE_LIMIT_COOLDOWN - elapsed)
            return False, f"Please wait {remaining} seconds before analyzing another CV."
            
    return True, ""

def record_run(client_ip: str):
    """Log a successful run for rate limiting."""
    now = time.time()
    st._global_rate_limits[client_ip] = now
    st._global_daily_runs.append(now)

def extract_text_from_file(uploaded_file) -> str:
    """Extract text from uploaded TXT, PDF, or DOCX file."""
    name = uploaded_file.name.lower()
    if name.endswith(".txt"):
        return str(uploaded_file.read(), "utf-8")
    elif name.endswith(".pdf"):
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    elif name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    return ""

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-header">Kenyan Hiring Agent 🇰🇪</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Multi-agent CV screening powered by Gemini 3.5 Flash (High Thinking)</div>', unsafe_allow_html=True)

# ── API Status Check ──────────────────────────────────────────────────────────
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_google_api_key_here":
    st.warning("⚠️ Google API Key not configured. Please add GOOGLE_API_KEY to your Streamlit secrets or .env file.")
    st.stop()

# ── UI Layout ─────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Candidate CV")
    uploaded_file = st.file_uploader("Upload CV (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])
    
    cv_placeholder = ""
    if uploaded_file is not None:
        with st.spinner("Extracting file text..."):
            cv_placeholder = extract_text_from_file(uploaded_file)
            if len(cv_placeholder) > MAX_CHARS:
                st.warning(f"⚠️ CV text was truncated to {MAX_CHARS} characters to prevent excessive API costs.")
                cv_placeholder = cv_placeholder[:MAX_CHARS]

    cv_text = st.text_area(
        "Or paste CV text directly here:",
        value=cv_placeholder,
        height=300,
        placeholder="Paste plain text CV here..."
    )

with col2:
    st.subheader("📋 Job Description")
    st.write("") # Spacer to align with file uploader on the left
    st.write("") 
    st.write("") 
    jd_text = st.text_area(
        "Paste Job Description text here:",
        height=300,
        placeholder="Paste requirements, role details, and education needs..."
    )
    if len(jd_text) > MAX_CHARS:
        st.warning(f"⚠️ Job description was truncated to {MAX_CHARS} characters.")
        jd_text = jd_text[:MAX_CHARS]

# ── Run Action ────────────────────────────────────────────────────────────────
st.write("")
if st.button("Analyse Candidate Fit"):
    if not cv_text.strip():
        st.error("Please upload or paste a CV.")
    elif not jd_text.strip():
        st.error("Please paste a Job Description.")
    else:
        # Rate limit checks
        ip = get_client_ip()
        allowed, err_msg = check_rate_limits(ip)
        
        if not allowed:
            st.error(err_msg)
        else:
            # Success, run the pipeline!
            status_container = st.container()
            
            try:
                # Stage 1: Extraction
                with status_container.status("Running evaluation pipeline...", expanded=True) as status:
                    status.write("Stage 1: Parsing CV details...")
                    cv_data = extract_cv(cv_text)
                    status.write(f"✓ Extracted data for: {cv_data.get('name', 'Unknown')}")
                    
                    # Stage 2: Scoring
                    status.write("Stage 2: Scoring CV against Job Description...")
                    score = score_candidate(cv_data, jd_text)
                    overall = score.get("overall_score", 0)
                    rec = score.get("recommendation", "maybe").upper()
                    status.write(f"✓ Fit Evaluation: {overall}/100 ({rec})")
                    
                    # Stage 3: Report
                    status.write("Stage 3: Generating final hiring report...")
                    report = generate_report(cv_data, score, jd_text)
                    
                    status.update(label="Evaluation Complete!", state="complete", expanded=False)
                
                # Record successful run for rate limiting
                record_run(ip)
                
                # Display Results
                st.subheader("📋 Hiring Recommendation Memo")
                st.markdown(f'<div class="report-box">{report}</div>', unsafe_allow_html=True)
                
                # Download Button
                st.download_button(
                    label="Download Report as Text",
                    data=report,
                    file_name=f"hiring_report_{cv_data.get('name', 'candidate').replace(' ', '_').lower()}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Pipeline error: {e}")
                st.info("This might be due to API connection limits or structural formatting changes. Please try again.")
