from src.pipeline import extract_info, match_profile, score_candidate, explain
from data.data import RESUMES, JOB_SKILLS

for name, resume in RESUMES.items():
    print("\n==============================")
    print(f"Candidate: {name}")

    extracted = extract_info(resume)
    print("Extracted:", extracted)

    matched = match_profile(extracted, JOB_SKILLS)
    print("Match:", matched)

    score, level = score_candidate(matched, extracted["experience"])
    print(f"Score: {score}/100 | Level: {level}")

    explanation = explain(score, matched)
    print("Explanation:", explanation)
