def calculate_risk(keyword_hits, iocs):
    score = 0

    score += len(keyword_hits) * 15
    score += len(iocs["urls"]) * 20
    score += len(iocs["ips"]) * 20

    if score >= 60:
        return "HIGH"
    elif score >= 30:
        return "MEDIUM"
    return "LOW"
