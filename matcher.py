"""
Resume/Job Description Matcher - Core Logic
--------------------------------------------
"""

import re

STOPWORDS = {
    "the", "is", "at", "which", "on", "a", "an", "and", "or", "in", "to",
    "of", "for", "with", "as", "by", "this", "that", "it", "are", "was",
    "be", "been", "has", "have", "had", "will", "would", "can", "could",
    "we", "you", "your", "our", "i", "he", "she", "they", "them", "from",
    "but", "not", "all", "any", "if", "so", "up", "out", "about"
}


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    return text


def extract_keywords(text: str) -> set:
    cleaned = clean_text(text)
    words = cleaned.split()
    keywords = {w for w in words if w not in STOPWORDS and len(w) > 2}
    return keywords


def compare(resume_text: str, job_text: str) -> dict:
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    matched = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords

    match_percent = 0
    if len(job_keywords) > 0:
        match_percent = round((len(matched) / len(job_keywords)) * 100, 1)

    return {
        "match_percent": match_percent,
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
    }


def main():
    sample_resume = """
    Experienced software developer skilled in Python, SQL, and HTML.
    Built a secure e-commerce platform as a final year project.
    Completed a certification in Generative AI. Strong problem solving skills.
    """

    sample_job = """
    We are looking for a Python developer with knowledge of SQL databases,
    machine learning, NLP, and cloud deployment. Experience with Git and
    REST APIs is a plus. Strong communication and teamwork skills required.
    """

    result = compare(sample_resume, sample_job)

    print(f"Match Percentage: {result['match_percent']}%")
    print(f"\nMatched Keywords ({len(result['matched_keywords'])}):")
    print(", ".join(result['matched_keywords']))
    print(f"\nMissing Keywords ({len(result['missing_keywords'])}):")
    print(", ".join(result['missing_keywords']))


if __name__ == "__main__":
    main()
