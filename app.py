
import streamlit as st
from urllib.parse import urlparse
import re

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 Phishing URL Detector")
st.write("Enter a URL below to check its suspicious patterns.")

url = st.text_input(
    "Enter URL",
    placeholder="https://example.com"
)

if st.button("Check URL"):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        check_url = url.strip()

        if not check_url.startswith(("http://", "https://")):
            check_url = "http://" + check_url

        parsed = urlparse(check_url)
        domain = parsed.netloc.lower()
        full_url = check_url.lower()

        uses_https = parsed.scheme == "https"
        has_ip = bool(
            re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain)
        )
        has_at = "@" in domain
        url_length = len(check_url)
        num_dots = domain.count(".")

        suspicious_words = [
            "login", "verify", "update",
            "password", "account", "secure"
        ]

        found_words = [
            word for word in suspicious_words
            if word in full_url
        ]

        score = 0
        if not uses_https:
            score += 1
        if has_ip:
            score += 2
        if has_at:
            score += 2
        if url_length > 75:
            score += 1
        if found_words:
            score += 1

        risk_score = round(score / 7 * 100, 2)

        st.subheader("Result")

        if score >= 2:
            st.error("Potentially Suspicious URL")
        else:
            st.success("No flagged patterns found")

        st.write(f"**Rule-based Risk Score:** {risk_score}%")

        st.subheader("Extracted Features")

        features = {
            "Uses HTTPS": int(uses_https),
            "URL Length": url_length,
            "Number of Dots in Domain": num_dots,
            "Has IP Address as Domain": int(has_ip),
            "Contains @ in Domain": int(has_at),
            "Suspicious Words Found": found_words
        }

        st.json(features)

        st.caption(
            "Educational prototype only. "
            "This tool cannot confirm whether a website is safe."
        )
