# Portfolio — Flask Web App

A personal portfolio website built with **Flask** (Python) to showcase skills, GitHub activity, and provide a contact form.

## Project Structure

```
portfolio/
├── app.py                 ← Flask application (routes, logic, email)
├── requirements.txt       ← Python dependencies
├── .env                   ← Secret config (email credentials)
├── .gitignore             ← Files Git should ignore
├── templates/
│   ├── base.html          ← Shared layout (nav, footer)
│   └── index.html         ← Main portfolio page
└── static/
    ├── css/style.css      ← Styling
    └── js/main.js         ← Interactive behavior
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open in browser
# http://127.0.0.1:5000
```

## Flask Concepts Used

| Concept | Where | What it does |
|---------|-------|-------------|
| Routes (`@app.route`) | `app.py` | Maps URLs to Python functions |
| Templates (`render_template`) | `templates/` | Renders HTML with dynamic data |
| Jinja2 (`{{ }}`, `{% %}`) | `.html` files | Template engine for loops, variables |
| Static files (`url_for`) | `static/` | Serves CSS, JS, images |
| Flash messages (`flash`) | `app.py` | One-time notifications |
| Form handling (`request.form`) | `app.py` | Reads submitted form data |
| Environment vars (`dotenv`) | `.env` | Keeps secrets out of code |

## Email Setup (Optional)

To enable the contact form to send real emails:

1. Go to your Google Account → Security → Enable 2-Step Verification
2. Visit https://myaccount.google.com/apppasswords
3. Generate an App Password for "Mail"
4. Update `.env` with your credentials