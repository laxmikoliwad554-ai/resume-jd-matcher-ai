# 📄 Resume / Job Description Matcher

A simple AI-powered web app that compares your resume against a job description and shows how well they match — built with Python and Streamlit.

## What it does

Paste your resume text and a job description into the app, and it will:
- Calculate a **match percentage** based on shared keywords
- Show which important keywords from the job description are **matched** in your resume
- Show which keywords are **missing**, so you know what to add (if you genuinely have that skill)

## How it works

The matcher extracts meaningful keywords from both texts (filtering out common stopwords like "the", "and", "with"), then compares the two keyword sets to calculate an overlap percentage. This gives a quick, rough estimate of how well a resume aligns with a job posting's language.

## Tech stack

- **Python**
- **Streamlit** — for the web interface
- **Regex** — for text cleaning and keyword extraction

## Running it locally

1. Clone this repository
2. Install dependencies:
3. 3. Run the app:
   4. 4. Open the local URL Streamlit gives you in your browser

## Example

Paste a resume and job description into the two text boxes and click **"Check Match"** to see your score, matched keywords, and missing keywords.

## Future improvements

- Support uploading PDF/DOCX resumes directly (pdfplumber is already in requirements)
- Weight keywords by importance instead of treating all matches equally
- Use NLP techniques (e.g. embeddings) for smarter semantic matching instead of exact keyword overlap
