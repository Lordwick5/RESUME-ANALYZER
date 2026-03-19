from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text

def extract_skills(text):
    skills_list = [
        "python", "java", "c", "c++", "html", "css", "javascript",
        "react", "node", "sql", "mongodb", "git", "fastapi"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills

def score_resume(skills, text):
    score = 0

    # Score based on number of skills
    score += len(skills) * 10

    # Bonus for resume length
    if len(text) > 1000:
        score += 20

    # Cap score at 100
    return min(score, 100)

def generate_suggestions(skills, text):
    suggestions = []

    if len(skills) < 3:
        suggestions.append("Add more technical skills to improve your profile.")

    if "project" not in text.lower():
        suggestions.append("Include projects to showcase practical experience.")

    if len(text) < 500:
        suggestions.append("Resume seems short. Add more details about your experience.")

    return suggestions