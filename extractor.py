import re
import tldextract

URL_REGEX = r"https?://[^\s]+"
IP_REGEX = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

def extract_iocs(text: str):
    urls = re.findall(URL_REGEX, text)
    ips = re.findall(IP_REGEX, text)

    domains = []
    for url in urls:
        ext = tldextract.extract(url)
        domains.append(f"{ext.domain}.{ext.suffix}")

    return {
        "urls": list(set(urls)),
        "domains": list(set(domains)),
        "ips": list(set(ips))
    }