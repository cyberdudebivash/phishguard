import sys
from rich import print
from phishing_analyzer import analyze_content
from extractor import extract_iocs
from scorer import calculate_risk
from response import response_actions

if len(sys.argv) != 2:
    print("[red]Usage:[/red] python cli.py input.txt")
    sys.exit(1)

text = open(sys.argv[1], encoding="utf-8").read()

keywords = analyze_content(text)
iocs = extract_iocs(text)
risk = calculate_risk(keywords, iocs)

print("[bold]PhishGuard AI Report[/bold]")
print(f"Risk Level: [yellow]{risk}[/yellow]")
print(f"Keyword Indicators: {keywords}")
print(f"IOCs: {iocs}")
print("Recommended Actions:")
for r in response_actions(risk):
    print(f"- {r}")
