import pdfplumber
import re


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def extract_fields(text):
    expected_fields = [
        "Policy Number",
        "Policyholder Name",
        "Effective Dates",
        "Date",
        "Time",
        "Location",
        "Description",
        "Claimant",
        "Third Parties",
        "Contact Details",
        "Asset Type",
        "Asset ID",
        "Estimated Damage",
        "Claim Type",
        "Attachments",
        "Initial Estimate"
    ]

    fields = {}

    for line in text.splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if key in expected_fields:
            fields[key] = value

    # If any expected field is found in multiline text, preserve it
    if "Description" not in fields:
        description_match = re.search(r"Description\s*:\s*(.+)", text, flags=re.IGNORECASE | re.DOTALL)
        if description_match:
            fields["Description"] = description_match.group(1).strip()

    return fields


def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text