# ============================================================
# FILE: 7.pydantic_Nested_Models.py
# TOPIC: Nested Models — composing models within other models
# ============================================================

# Nested models allow you to compose multiple BaseModel classes together
# This creates a hierarchy where one model contains another model as a field
# Pydantic automatically validates nested structures recursively
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Annotated, Optional, Any

class Address(BaseModel):
    # Address is a nested model used inside Patient
    street: Annotated[str, Field(min_length=1, title="Street", description="Street address", json_schema_extra={"example": "123 Main St"})]
    city: Annotated[str, Field(min_length=1, title="City", description="City name", json_schema_extra={"example": "Anytown"})]
    zip_code: Annotated[str, Field(min_length=5, max_length=10, title="Zip Code", description="Postal code", json_schema_extra={"example": "12345"})]

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50, title="Patient Name", description="The name of the patient", json_schema_extra={"example": "John Doe"})]

    age: Annotated[int, Field(gt=0, lt=120, title="Patient Age", description="The age of the patient", json_schema_extra={"example": 30})]

    email: Annotated[EmailStr, Field(title="Patient Email", description="The email address of the patient", json_schema_extra={"example": "c7c2A@example.com"})]

    LinkedIn: Annotated[AnyUrl, Field(title="Patient LinkedIn", description="The LinkedIn profile URL of the patient", json_schema_extra={"example": "https://www.linkedin.com/in/johndoe"})]

    weight: Annotated[float, Field(gt=0, lt=500, title="Patient Weight", description="The weight of the patient in kg", json_schema_extra={"example": 70.5})]

    married: Annotated[Optional[bool], Field(default=False, title="Patient Married", description="Marital status of the patient", json_schema_extra={"example": True})]

    allergies: Annotated[List[str], Field(title="Patient Allergies", description="List of patient allergies", json_schema_extra={"example": ["penicillin", "latex"]})]

    contact: Annotated[Dict[str, str], Field(title="Patient Contact", description="Contact information for the patient", json_schema_extra={"example": {"email": "c7c2A@example.com", "phone": "123-456-7890"}})]

    # address is a nested Address model — pydantic validates it recursively
    address: Address

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
    print(f"Patient Address: {patient.address.street}, {patient.address.city}, {patient.address.zip_code}")

patientinfo: Dict[str, Any] = {
    "name": "John Doe",
    "age": 20,
    "email": "c7c2A@example.com",
    "LinkedIn": "https://www.linkedin.com/in/johndoe",
    "weight": 70.5,
    "married": True,
    "allergies": ["penicillin", "latex"],
    "contact": {"email": "c7c2A@example.com", "phone": "123-456-7890"},
    "address": {"street": "123 Main St", "city": "Anytown", "zip_code": "12345"}
}

patient1 = Patient(**patientinfo)
update_patient_info(patient1)
