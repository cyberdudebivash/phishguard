def response_actions(risk):
    if risk == "HIGH":
        return [
            "Isolate affected account",
            "Reset credentials immediately",
            "Block URLs/domains",
            "Check for lateral movement",
            "Notify security team"
        ]
    if risk == "MEDIUM":
        return [
            "Warn user",
            "Block sender/domain",
            "Monitor account activity"
        ]
    return [
        "Educate user",
        "Monitor for repeat attempts"
    ]
