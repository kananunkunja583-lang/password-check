from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special character")

    if score == 5:
        return "Strong ✅", feedback
    elif score >= 3:
        return "Moderate ⚠️", feedback
    else:
        return "Weak ❌", feedback


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    tips = []

    if request.method == "POST":
        password = request.form["password"]
        result, tips = check_password_strength(password)

    return render_template("index.html", result=result, tips=tips)


if __name__ == "__main__":
    app.run(debug=True)