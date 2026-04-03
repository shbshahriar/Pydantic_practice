# ============================================================
# FILE: 4.pydantic_Field_Validator.py
# TOPIC: field_validator — custom validation logic on individual fields
# ============================================================

# field_validator lets you write custom logic to validate a single field
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, ValidationError
from typing import List, Dict, Annotated, Optional, Any

class Patient(BaseModel):
    # Annotated combines the type with Field metadata in one place
    # Field() adds constraints and schema info (title, description, example for docs)
    name: Annotated[str, Field(min_length=2, max_length=50, title="Patient Name", description="The name of the patient", json_schema_extra={"example": "John Doe"})]

    # strict=True means pydantic will NOT try to coerce types — e.g., "20" (str) won't be accepted as int
    age: Annotated[int, Field(strict=True, gt=0, lt=120, title="Patient Age", description="The age of the patient", json_schema_extra={"example": 30})]

    # EmailStr validates that the value is a properly formatted email address
    email: Annotated[EmailStr, Field(title="Patient Email", description="The email address of the patient", json_schema_extra={"example": "c7c2A@example.com"})]

    # AnyUrl validates that the value is a valid URL
    LinkedIn: Annotated[AnyUrl, Field(title="Patient LinkedIn", description="The LinkedIn profile URL of the patient", json_schema_extra={"example": "https://www.linkedin.com/in/johndoe"})]

    weight: Annotated[float, Field(gt=0, lt=500, title="Patient Weight", description="The weight of the patient in kg", json_schema_extra={"example": 70.5})]

    # Optional[bool] means the field can be bool OR None — default=False means it's not required
    married: Annotated[Optional[bool], Field(default=False, title="Patient Married", description="Marital status of the patient", json_schema_extra={"example": True})]

    allergies: Annotated[List[str], Field(title="Patient Allergies", description="List of patient allergies", json_schema_extra={"example": ["penicillin", "latex"]})]

    contact: Annotated[Dict[str, str], Field(title="Patient Contact", description="Contact information for the patient", json_schema_extra={"example": {"email": "c7c2A@example.com", "phone": "123-456-7890"}})]

    # @field_validator targets a specific field ('email') and runs after pydantic's built-in validation
    # mode="after" means this runs after EmailStr has already confirmed it's a valid email format
    @field_validator('email', mode="after")
    @classmethod  # must be a classmethod — pydantic calls it on the class, not an instance
    def validate_email(cls, value):
        # Custom rule: email must come from the domain example.com
        if not value.endswith('@example.com'):
            raise ValueError('Email must be from the domain example.com')
        return value  # always return the value if validation passes

    # Another field_validator — this one runs custom logic on the 'age' field
    @field_validator('age', mode="after")
    @classmethod
    def validate_age(cls, value):
        # Custom rule: patient must be at least 18 years old
        if value < 18:
            raise ValueError('Patient must be at least 18 years old')
        return value

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

# Dict[str, Any] means keys are strings but values can be anything
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

# try/except ValidationError — catches failures from:
# 1. type checks  2. Field constraints (gt, lt, strict)  3. custom field_validators
# Pydantic runs them in that order and collects ALL errors before raising
try:
    patient1 = Patient(**patientinfo)
    update_patient_info(patient1)
except ValidationError as e:
    # e.errors() shows each failed field, the error type, and the message from raise ValueError(...)
    print(f"Validation Error: {e.errors()}")
