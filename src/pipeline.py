import re

def extract_info(resume):
    skills = []
    skill_keywords = ["python", "machine learning", "nlp", "sql", "excel", "deep learning"]

    for skill in skill_keywords:
        if skill in resume.lower():
            skills.append(skill)

    exp_match = re.search(r"(\d+)\s*years", resume.lower())
    experience = int(exp_match.group(1)) if exp_match else 0

    return {"skills": skills, "experience": experience}


def match_profile(profile, job_skills):
    matched = [s for s in profile["skills"] if s in job_skills]
    missing = [s for s in job_skills if s not in profile["skills"]]

    return {"matched": matched, "missing": missing}


def score_candidate(match, experience):
    skill_score = (len(match["matched"]) / 4) * 70
    exp_score = min(experience / 5, 1) * 40

    score = int(skill_score + exp_score)
    score = min(score, 100)

    if score >= 75:
        level = "Strong"
    elif score >= 40:
        level = "Average"
    else:
        level = "Weak"

    return score, level


def explain(score, match):
    return (
        f"The candidate matches {len(match['matched'])} required skills "
        f"and lacks {len(match['missing'])}. "
        f"The score reflects both skill alignment and experience level."
    )
