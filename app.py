import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Create the Flask app ---
app = Flask(__name__)

# Secret key is needed for flash messages (session security)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")


PROFILE = {
    "name": "Hari Prasad",
    "title": "Cloud DevOps Engineer",
    "bio": (
        "Cloud DevOps Engineer with 5 years of experience in designing, automating, "
        "and optimizing mission-critical deployments primarily in Microsoft Azure. "
        "Skilled in CI/CD pipeline development, AKS, Infrastructure as Code (IaC), "
        "and cloud security. Demonstrated ability to improve system reliability, "
        "accelerate delivery cycles, and enhance DevOps efficiency in enterprise-scale "
        "environments. Actively interested in expanding expertise in AWS to build "
        "cross-platform cloud solutions and drive innovation across hybrid cloud "
        "infrastructures. Also an MLOps enthusiast, passionate about bridging the gap "
        "between machine learning and operations to deliver scalable AI solutions."
    ),
    "github": "https://github.com/hariprasadgowda",
    "linkedin": "https://www.linkedin.com/in/hari-prasad-/", 
    "email": "hariprasadgowda1998@gmail.com",  
}

# Tools/Skills with icon names from https://devicon.dev (free dev icons)
SKILLS = [
    {"name": "Azure", "icon": "azure"},
    {"name": "AWS", "icon": "amazonwebservices"},
    {"name": "Azure DevOps", "icon": "azuredevops"},
    {"name": "Terraform", "icon": "terraform"},
    {"name": "Azure Bicep", "icon": "azure"},
    {"name": "Kubernetes", "icon": "kubernetes"},
    {"name": "Docker", "icon": "docker"},
    {"name": "GitHub Actions", "icon": "githubactions"},
    {"name": "Prometheus", "icon": "prometheus"},
    {"name": "Grafana", "icon": "grafana"},
    {"name": "Helm", "icon": "helm"},
    {"name": "PowerShell", "icon": "powershell"},
    {"name": "Python", "icon": "python"},
    {"name": "Flask", "icon": "flask"},
    {"name": "Git", "icon": "git"},
    {"name": "GitHub", "icon": "github"},
    {"name": "HTML5", "icon": "html5"},
    {"name": "CSS3", "icon": "css3"},
    {"name": "JavaScript", "icon": "javascript"},
    {"name": "VS Code", "icon": "vscode"},
]


@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE, skills=SKILLS)


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    # --- Validation ---
    if not name or not email or not message:
        # flash() stores a message that shows ONCE on the next page load
        flash("Please fill in all fields!", "error")
        return redirect(url_for("home") + "#contact")

    # --- Send Email ---
    email_sent = send_email(name, email, message)

    if email_sent:
        flash("Thanks for reaching out! I'll get back to you soon.", "success")
    else:
        flash("Oops! Something went wrong. Please try again later.", "error")

    # redirect() sends the user to a different page
    # url_for('home') generates the URL for the home() function → '/'
    return redirect(url_for("home") + "#contact")


# ============================================================
# EMAIL HELPER
# ============================================================

def send_email(sender_name, sender_email, message_body):
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL", PROFILE["email"])

    # If email is not configured, log it and return False
    if not smtp_username or not smtp_password:
        print("Email not configured! Set SMTP_USERNAME and SMTP_PASSWORD in .env")
        print(f"   Message from {sender_name} ({sender_email}): {message_body}")
        return False

    try:
        # Build the email
        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = recipient_email
        msg["Subject"] = f"Portfolio Contact: Message from {sender_name}"

        body = (
            f"Name: {sender_name}\n"
            f"Email: {sender_email}\n\n"
            f"Message:\n{message_body}"
        )
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Encrypt the connection
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        print(f"Email sent from {sender_name} ({sender_email})")
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


# ============================================================
# RUN THE APP
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
