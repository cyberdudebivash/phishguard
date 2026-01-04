import sys
import os
from flask import Flask, render_template, request


# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from phishing_analyzer import analyze_content
from extractor import extract_iocs
from scorer import calculate_risk
from response import response_actions


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        content = request.form.get("content", "")

        keywords = analyze_content(content)
        iocs = extract_iocs(content)
        risk = calculate_risk(keywords, iocs)
        actions = response_actions(risk)

        result = {
            "risk": risk,
            "keywords": keywords,
            "iocs": iocs,
            "actions": actions
        }

    return render_template("report.html", result=result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
