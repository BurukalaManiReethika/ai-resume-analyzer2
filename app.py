import streamlit as st
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume

# ── Page Configuration ──────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🧠",
    layout="wide"
)

# ── Header ───────────────────────────────────────────────────
st.title("🧠 AI Resume Analyzer")
st.markdown("Upload your resume and paste a job description to get an **AI-powered match score** and improvement tips.")
st.divider()

# ── Input Section ────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Only PDF files are supported"
    )

with col2:
    st.subheader("💼 Paste Job Description")
    job_description = st.text_area(
        "Job Description",
        height=250,
        placeholder="Paste the full job description here..."
    )

st.divider()

# ── Analyze Button ───────────────────────────────────────────
analyze_btn = st.button("🔍 Analyze My Resume", type="primary", use_container_width=True)

# ── Results Section ──────────────────────────────────────────
if analyze_btn:

    # Validation
    if not uploaded_file:
        st.error("⚠️ Please upload your resume PDF first.")
        st.stop()

    if not job_description.strip():
        st.error("⚠️ Please paste a job description.")
        st.stop()

    if len(job_description.strip()) < 50:
        st.warning("⚠️ Job description seems too short. Add more details for better results.")

    # Extract resume text
    with st.spinner("📖 Reading your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    if not resume_text:
        st.error("❌ Could not extract text from your PDF. Make sure it's not a scanned image.")
        st.stop()

    # Analyze with AI
    with st.spinner("🤖 AI is analyzing your resume... (this takes 10-15 seconds)"):
        result = analyze_resume(resume_text, job_description)

    # ── Display Results ──────────────────────────────────────
    st.success("✅ Analysis Complete!")
    st.divider()

    # Match Score
    score = result.get("match_score", 0)

    if score >= 75:
        score_color = "green"
        score_emoji = "🟢"
        score_label = "Strong Match"
    elif score >= 50:
        score_color = "orange"
        score_emoji = "🟡"
        score_label = "Moderate Match"
    else:
        score_color = "red"
        score_emoji = "🔴"
        score_label = "Weak Match"

    st.markdown(f"## {score_emoji} Match Score: **:{score_color}[{score}% — {score_label}]**")
    st.progress(score / 100)

    st.divider()

    # Three columns for results
    r1, r2, r3 = st.columns(3)

    with r1:
        st.subheader("✅ Matched Skills")
        matched = result.get("matched_skills", [])
        if matched:
            for skill in matched:
                st.success(f"✔ {skill}")
        else:
            st.info("No strong skill matches found.")

    with r2:
        st.subheader("❌ Missing Skills")
        missing = result.get("missing_skills", [])
        if missing:
            for skill in missing:
                st.error(f"✖ {skill}")
        else:
            st.success("No critical gaps found!")

    with r3:
        st.subheader("💡 Suggestions")
        suggestions = result.get("suggestions", [])
        if suggestions:
            for i, tip in enumerate(suggestions, 1):
                st.info(f"{i}. {tip}")

    st.divider()

    # Summary
    st.subheader("📝 Overall Summary")
    st.write(result.get("summary", "No summary available."))
