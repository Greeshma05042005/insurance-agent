from fastapi import FastAPI, UploadFile, File
import shutil
import os

from extractor import read_txt, read_pdf, extract_fields
from validator import validate_fields
from router import get_route

app = FastAPI()


@app.post("/process-claim")
async def process_claim(file: UploadFile = File(...)):

    # Save uploaded file
    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read file
    if file.filename.endswith(".txt"):
        text = read_txt(file_path)

    elif file.filename.endswith(".pdf"):
        text = read_pdf(file_path)

    else:
        os.remove(file_path)
        return {"error": "Only PDF and TXT files are allowed."}

    # Extract information
    fields = extract_fields(text)

    # Validate
    missing = validate_fields(fields)

    # Route
    route, reason = get_route(fields, missing)

    # Delete uploaded file
    os.remove(file_path)

    return {
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }