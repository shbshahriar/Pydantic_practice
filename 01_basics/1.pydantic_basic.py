# ============================================================
# FILE: 1.pydantic_basic.py
# TOPIC: Pydantic Basics — Defining a simple model and using it
# ============================================================

from pydantic import BaseModel, ValidationError
from typing import TypedDict

# TypedDict is a plain Python typing tool — it defines the shape of a dictionary
# It does NOT validate at runtime, it is only for type checkers (like mypy/pyright)
class PatientInfo(TypedDict):
    name: str
    age: int

# Pydantic model — inherits from BaseModel
# Unlike TypedDict, pydantic ACTUALLY validates types at runtime when you create an instance
class patient(BaseModel):
    name: str   # must be a string
    age: int    # must be an integer — pydantic raises ValidationError if wrong type is passed

# Function to display patient info — accepts a patient object
def inserted_patient_info(patient: patient):
    print(f"Patient Name: {patient.name}")   # access fields using dot notation
    print(f"Patient Age: {patient.age}")
    print("Patient information inserted successfully.")

# Function to update patient info — modifies fields directly and prints them
def update_patient_info(patient: patient):
    patient.age = 30   # overwrite the age field after model creation
    print("Patient information updated successfully.")
    print(f"Updated Patient Age: {patient.age}")
    print(f"Patient Name: {patient.name}")

# PatientInfo TypedDict is used here as the type hint for the dictionary
# This helps the type checker understand what keys/values are expected
patientinfo: PatientInfo = {
    "name": "John Doe",
    "age": 20}

# try/except ValidationError — catches any validation errors pydantic raises
# ValidationError is raised when a field value fails its type check
try:
    # ** unpacks the dictionary into keyword arguments
    # Equivalent to: patient1 = patient(name="John Doe", age=20)
    # Pydantic validates types here — wrong types would raise a ValidationError
    patient1 = patient(**patientinfo)
    # Call update function — changes age to 30 and prints updated info
    update_patient_info(patient1)
except ValidationError as e:
    # e.errors() returns a list of dicts — each dict describes one validation failure
    # It tells you: which field failed, what the error message is, and what value was given
    print(f"Validation Error: {e.errors()}")
