# ============================================================
# FILE: 3.pydantic_Field_Annoted.py
# TOPIC: Annotated + Field — adding constraints and metadata to fields
# ============================================================

# Field() lets you add constraints (min_length, gt, lt etc.) and metadata (title, description)
# EmailStr validates proper email format (requires: pip install pydantic[email])
# AnyUrl validates that the value is a valid URL
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Annotated, Optional, Any

class Patient(BaseModel):
    # Annotated[type, Field(...)] is the Pydantic V2 way to combine type + constraints in one place
    # min_length=2, max_length=50 → string must be between 2 and 50 characters
    # title, description → used in JSON schema / API docs (e.g. FastAPI)
    # json_schema_extra={"example": ...} → provides an example value in the schema (V2 correct way)
    name: Annotated[str, Field(min_length=2, max_length=50, title="Patient Name", description="The name of the patient", json_schema_extra={"example": "John Doe"})]

    # gt=0 means "greater than 0", lt=120 means "less than 120"
    age: Annotated[int, Field(gt=0, lt=120, title="Patient Age", description="The age of the patient", json_schema_extra={"example": 30})]

    # EmailStr checks the value is a valid email address format (e.g. user@domain.com)
    email: Annotated[EmailStr, Field(title="Patient Email", description="The email address of the patient", json_schema_extra={"example": "c7c2A@example.com"})]

    # AnyUrl checks the value is a valid URL (http, https, ftp, etc.)
    LinkedIn: Annotated[AnyUrl, Field(title="Patient LinkedIn", description="The LinkedIn profile URL of the patient", json_schema_extra={"example": "https://www.linkedin.com/in/johndoe"})]

    # gt=0, lt=500 → weight must be between 0 and 500 (exclusive)
    weight: Annotated[float, Field(gt=0, lt=500, title="Patient Weight", description="The weight of the patient in kg", json_schema_extra={"example": 70.5})]

    # Optional[bool] means the value can be True, False, or None
    # default=False means this field is not required — it defaults to False if not provided
    married: Annotated[Optional[bool], Field(default=False, title="Patient Married", description="Marital status of the patient", json_schema_extra={"example": True})]

    # List[str] → a list where every item must be a string
    allergies: Annotated[List[str], Field(title="Patient Allergies", description="List of patient allergies", json_schema_extra={"example": ["penicillin", "latex"]})]

    # Dict[str, str] → a dictionary where both keys and values must be strings
    contact: Annotated[Dict[str, str], Field(title="Patient Contact", description="Contact information for the patient", json_schema_extra={"example": {"email": "c7c2A@example.com", "phone": "123-456-7890"}})]

# Function to print all patient fields using dot notation
def update_patient_info(patient: Patient):
    print("Patient information updated successfully.")
    print(f"Updated Patient Age: {patient.age}")
    print(f"Patient Name: {patient.name}")
    print(f"Patient Email: {patient.email}")
    print(f"Patient LinkedIn: {patient.LinkedIn}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact: {patient.contact}")

# Dict[str, Any] → keys are strings, values can be anything (int, str, list, etc.)
patientinfo: Dict[str, Any] = {
    "name": "John Doe",
    "age": 20,
    "email": "c7c2A@example.com",
    "LinkedIn": "https://www.linkedin.com/in/johndoe",
    "weight": 70.5,
    "married": True,
    "allergies": ["penicillin", "latex"],
    "contact": {"email": "c7c2A@example.com", "phone": "123-456-7890"}
}

# ** unpacks the dictionary — pydantic runs all Field constraints and type checks here
patient1 = Patient(**patientinfo)
update_patient_info(patient1)
