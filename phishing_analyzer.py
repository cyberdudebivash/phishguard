PHISHING_KEYWORDS = [
    "urgent", "verify", "suspended", "action required",
    "reset password", "confirm immediately", "login now"
]

def analyze_content(text: str):
    hits = []
    for word in PHISHING_KEYWORDS:
        if word.lower() in text.lower():
            hits.append(word)
    return hits
