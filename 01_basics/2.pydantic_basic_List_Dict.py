# ============================================================
# FILE: 2.pydantic_basic_List_Dict.py
# TOPIC: Using complex types — List and Dict inside a pydantic model
# ============================================================

from pydantic import BaseModel, ValidationError
from typing import List, Dict  # List and Dict allow specifying the types inside collections

# Pydantic model with more complex field types
class patient(BaseModel):
    name: str
    age: int
    weight: float                # float allows decimal numbers (e.g., 70.5)
    married: bool                # boolean: True or False
    allergies: List[str]         # a list where every item must be a string
    contact: Dict[str, str]      # a dictionary where both keys and values must be strings

# Function to print all patient fields
def update_patient_info(patient: patient):
    print("Patient information updated successfully.")
    print(f"Updated Patient Age: {patient.age}")
    print(f"Patient Name: {patient.name}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")   # prints the full list
    print(f"Patient Contact: {patient.contact}")       # prints the full dictionary

# Raw dictionary — # type: ignore suppresses type checker warnings on this line
patientinfo = { # type: ignore
    "name": "John Doe",
    "age": 20,
    "weight": 70.5,
    "married": True,
    "allergies": ["penicillin", "latex"],              # list of strings
    "contact": {"home": "123 Main St", "work": "456 Business St"}  # dict of strings
}

# try/except ValidationError — catches any validation errors pydantic raises
try:
    # Unpack the dictionary into the pydantic model
    # Pydantic checks: allergies is a List[str]? Dict values are str? etc.
    patient1 = patient(**patientinfo) # type: ignore
    update_patient_info(patient1)
except ValidationError as e:
    # e.errors() returns a list — each item describes one field that failed validation
    print(f"Validation Error: {e.errors()}")
