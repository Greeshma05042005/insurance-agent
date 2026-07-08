# Autonomous Insurance Claims Processing Agent

## Overview

This project is a lightweight Insurance Claims Processing Agent built using **FastAPI**.

The application processes First Notice of Loss (FNOL) documents in **TXT** or **PDF** format, extracts important claim information, validates mandatory fields, applies business routing rules, and returns the results in JSON format.

---

## Features

- Upload FNOL documents (.txt or .pdf)
- Extract policy, incident, claimant, and asset details
- Detect missing mandatory fields
- Route claims based on business rules
- Return structured JSON response
- Interactive API documentation using Swagger UI

---

## Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- pdfplumber
- Regular Expressions (Regex)

---

## Project Structure

```
insurance-agent/
│
├── app.py
├── extractor.py
├── validator.py
├── router.py
├── models.py
├── requirements.txt
├── README.md
│
├── sample_docs/
│   └── claim1.txt
│
├── outputs/
│
└── venv/
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd insurance-agent
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

The API will start at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /process-claim

Upload a TXT or PDF FNOL document.

### Supported Formats

- TXT
- PDF

---

## Extracted Fields

### Policy Information

- Policy Number
- Policyholder Name
- Effective Dates

### Incident Information

- Date
- Time
- Location
- Description

### Involved Parties

- Claimant
- Third Parties
- Contact Details

### Asset Details

- Asset Type
- Asset ID
- Estimated Damage

### Other Fields

- Claim Type
- Attachments
- Initial Estimate

---

## Routing Rules

| Condition | Route |
|------------|----------------------|
| Missing mandatory fields | Manual Review |
| Description contains "fraud", "staged", or "inconsistent" | Investigation Flag |
| Claim Type = Injury | Specialist Queue |
| Estimated Damage < ₹25,000 | Fast-track |
| Otherwise | Standard Processing |

---

## Sample Response

```json
{
    "extractedFields": {
        "Policy Number": "POL12345",
        "Policyholder Name": "John Smith",
        "Effective Dates": "01-01-2026 to 31-12-2026",
        "Date": "05-07-2026",
        "Time": "10:30 AM",
        "Location": "Bangalore",
        "Description": "Minor collision with another vehicle.",
        "Claimant": "John Smith",
        "Third Parties": "David Lee",
        "Contact Details": "9876543210",
        "Asset Type": "Car",
        "Asset ID": "CAR001",
        "Estimated Damage": "18000",
        "Claim Type": "Vehicle",
        "Attachments": "Photos",
        "Initial Estimate": "18000"
    },
    "missingFields": [],
    "recommendedRoute": "Fast-track",
    "reasoning": "Estimated damage is below ₹25,000."
}
```

---

## Business Logic

1. Read uploaded PDF/TXT document.
2. Extract required fields using Regular Expressions.
3. Validate mandatory fields.
4. Apply routing rules.
5. Return structured JSON response.

---

## Future Improvements

- AI/LLM-based field extraction
- OCR support for scanned PDFs
- Database integration
- Authentication
- Claim history tracking
- Docker deployment

---

## Author

Greeshma