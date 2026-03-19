from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import shutil
import os

from utils import extract_text_from_pdf, extract_skills, score_resume, generate_suggestions

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"

# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Upload route
@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text_from_pdf(file_path)

    # AI processing
    skills = extract_skills(text)
    score = score_resume(skills, text)
    suggestions = generate_suggestions(skills, text)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": "File uploaded successfully!",
        "resume_text": text[:500],
        "skills": skills,
        "score": score,
        "suggestions": suggestions
    })