"""
Resume/Job Matcher - Streamlit App
-----------------------------------
"""

import streamlit as st
from matcher import compare

st.set_page_config(page_title="Resume Matcher AI", page_icon="📄")

st.title("📄 Resume / Job Description Matcher")
st.write("Paste your resume and a job description below to see your match score.")

col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area("Your Resume Text", height=300,
                                placeholder="Paste your resume content here...")

with col2:
    job_text = st.text_area("Job Description Text", height=300,
                             placeholder="Paste the job description here...")

if st.button("Check Match", type="primary"):
    if not resume_text.strip() or not job_text.strip():
        st.warning("Please paste both your resume and the job description.")
    else:
        result = compare(resume_text, job_text)

        st.subheader(f"Match Score: {result['match_percent']}%")
        st.progress(min(int(result['match_percent']), 100))

        c1, c2 = st.columns(2)
        with c1:
            st.success("✅ Matched Keywords")
            st.write(", ".join(result['matched_keywords']) or "None found")
        with c2:
            st.error("❌ Missing Keywords")
            st.write(", ".join(result['missing_keywords']) or "None missing!")

        st.info("Tip: Try adding some of the missing keywords to your resume "
                "(only if you genuinely have that skill/experience) to improve your match.")