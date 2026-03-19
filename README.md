# 🚀 AI Resume Analyzer

An AI-powered web application that analyzes resumes and provides insights such as skill extraction, resume scoring, and improvement suggestions.

---

## 🌐 Live Demo

👉 https://resume-analyzer-production-b824.up.railway.app

---

## 📌 Features

* 📄 Upload resume in PDF format
* 🧠 Extract text using PDF parsing
* 🛠️ Detect technical skills using NLP techniques
* 📊 Generate resume score based on content
* 💡 Provide improvement suggestions
* 🎯 Recommend job roles based on skills

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS (Jinja2 Templates)
* **Language:** Python
* **Libraries:**

  * PyPDF2 (PDF parsing)
  * FastAPI (API framework)
  * Uvicorn (ASGI server)

---

## 📂 Project Structure

```
resume-analyzer/
│
├── main.py
├── utils.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── uploads/
├── requirements.txt
└── Procfile
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/Lordwick5/RESUME-ANALYZER.git
cd RESUME-ANALYZER
```

### 2. Install dependencies

```
python -m pip install -r requirements.txt
```

### 3. Run the application

```
python -m uvicorn main:app --reload
```

### 4. Open in browser

```
http://127.0.0.1:8000
```

---

## 🚀 Deployment

This project is deployed using Railway.

Start command used:

```
uvicorn main:app --host=0.0.0.0 --port=$PORT
```

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. Application extracts text using PyPDF2
3. Skills are detected using keyword-based NLP
4. Resume is scored based on:

   * Number of skills
   * Content length
5. Suggestions are generated for improvement
6. Job roles are recommended based on skills

---

## 📸 Screenshots

*(Add screenshots here later for better presentation)*

---

## 📈 Future Improvements

* 🔍 Use advanced NLP (spaCy / transformers)
* 🎨 Improve UI with modern frameworks (React / Tailwind)
* 🗄️ Add database for storing resumes
* 🔐 User authentication system
* 📊 Analytics dashboard

---

## 👨‍💻 Author

**Prashant Chaudhary**

---

## ⭐ Acknowledgements

* Inspired by real-world recruitment systems
* Built as part of AI project preparation

---

## 📌 Note

This is a beginner-friendly AI project using rule-based NLP techniques and is intended for learning and demonstration purposes.
