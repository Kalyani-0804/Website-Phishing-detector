
from urllib.parse import urlparse

url = input("Enter a URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "http://" + url

parsed_url = urlparse(url)
domain = parsed_url.netloc.lower()

suspicious_words = [
    "login", "verify", "update", "secure",
    "account", "password", "free"
]

print("\n--- URL Analysis ---")

if parsed_url.scheme == "https":
    print("HTTPS: Yes")
else:
    print("HTTPS: No")

if "@" in url or parsed_url.username:
    print("Suspicious pattern: URL contains @")
else:
    print("Suspicious pattern: No @ found")

found_words = []

for word in suspicious_words:
    if word in domain:
        found_words.append(word)

if len(found_words) > 0:
    print("Suspicious words in domain:", found_words)
    print("Result: Potentially suspicious URL")
else:
    print("Suspicious words in domain: None")
    print("Result: No flagged domain pattern found")

print("Note: This is a basic rule-based check, not a guarantee of safety.")
