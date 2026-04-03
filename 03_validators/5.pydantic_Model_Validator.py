# ============================================================
# FILE: 5.pydantic_Model_Validator.py
# TOPIC: model_validator — validation that checks multiple fields together
# ============================================================

# Self is used as the return type hint for model_validator (refers to the model class itself)
from typing_extensions import Self

# model_validator runs validation on the entire model AFTER all fields are validated
from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, ValidationError
from typing import List, Dict, Annotated, Optional, Any

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50, title="Patient Name", description="The name of the patient", json_schema_extra={"example": "John Doe"})]

    age: Annotated[int, Field(strict=True, gt=0, lt=120, title="Patient Age", description="The age of the patient", json_schema_extra={"example": 30})]

    email: Annotated[EmailStr, Field(title="Patient Email", description="The email address of the patient", json_schema_extra={"example": "c7c2A@example.com"})]

    LinkedIn: Annotated[AnyUrl, Field(title="Patient LinkedIn", description="The LinkedIn profile URL of the patient", json_schema_extra={"example": "https://www.linkedin.com/in/johndoe"})]

    weight: Annotated[float, Field(gt=0, lt=500, title="Patient Weight", description="The weight of the patient in kg", json_schema_extra={"example": 70.5})]

    married: Annotated[Optional[bool], Field(default=False, title="Patient Married", description="Marital status of the patient", json_schema_extra={"example": True})]

    allergies: Annotated[List[str], Field(title="Patient Allergies", description="List of patient allergies", json_schema_extra={"example": ["penicillin", "latex"]})]

    contact: Annotated[Dict[str, str], Field(title="Patient Contact", description="Contact information for the patient", json_schema_extra={"example": {"email": "c7c2A@example.com", "phone": "123-456-7890"}})]

    # @model_validator runs after ALL fields have been validated
    # Unlike field_validator (single field), model_validator has access to the ENTIRE model
    # mode="after" means 'model' is already a fully constructed Patient instance
    @model_validator(mode="after")
    @classmethod
    def validate_emergency_contact(cls, model):
        # Cross-field rule: if age > 60, the contact dict must include an 'emergency_contact' key
        # This is only possible with model_validator because it checks two fields at once (age + contact)
        if model.age > 60 and "emergency_contact" not in model.contact:
            raise ValueError('Emergency contact is required for patients over 60 years old')
        return model  # always return the model if validation passes

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

patientinfo: Dict[str, Any] = {
    "name": "John Doe",
    "age": 20,           # age is 20 — under 60, so emergency_contact is NOT required
    "email": "c7c2A@example.com",
    "LinkedIn": "https://www.linkedin.com/in/johndoe",
    "weight": 70.5,
    "married": True,
    "allergies": ["penicillin", "latex"],
    "contact": {"email": "c7c2A@example.com", "phone": "123-456-7890"}
}

# try/except ValidationError — catches failures from field validation AND model_validator
# model_validator runs last — after all individual fields pass — so its errors appear here too
try:
    patient1 = Patient(**patientinfo)
    update_patient_info(patient1)
except ValidationError as e:
    # e.errors() will show the cross-field error raised inside validate_emergency_contact
    print(f"Validation Error: {e.errors()}")
