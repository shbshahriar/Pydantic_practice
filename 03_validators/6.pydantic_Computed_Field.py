# ============================================================
# FILE: 6.pydantic_Computed_Field.py
# TOPIC: computed_field — auto-calculated fields derived from other fields
# ============================================================

# computed_field lets you define a field whose value is calculated from other fields
# It is NOT passed in by the user — pydantic computes it automatically
from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Annotated, Optional, Any

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50, title="Patient Name", description="The name of the patient", json_schema_extra={"example": "John Doe"})]

    age: Annotated[int, Field(strict=True, gt=0, lt=120, title="Patient Age", description="The age of the patient", json_schema_extra={"example": 30})]

    email: Annotated[EmailStr, Field(title="Patient Email", description="The email address of the patient", json_schema_extra={"example": "c7c2A@example.com"})]

    LinkedIn: Annotated[AnyUrl, Field(title="Patient LinkedIn", description="The LinkedIn profile URL of the patient", json_schema_extra={"example": "https://www.linkedin.com/in/johndoe"})]

    weight: Annotated[float, Field(gt=0, lt=500, title="Patient Weight", description="The weight of the patient in kg", json_schema_extra={"example": 70.5})]

    # height is required as input — needed to compute BMI
    height: Annotated[float, Field(gt=0, lt=300, title="Patient Height", description="The height of the patient in cm", json_schema_extra={"example": 175.0})]

    married: Annotated[Optional[bool], Field(default=False, title="Patient Married", description="Marital status of the patient", json_schema_extra={"example": True})]

    allergies: Annotated[List[str], Field(title="Patient Allergies", description="List of patient allergies", json_schema_extra={"example": ["penicillin", "latex"]})]

    contact: Annotated[Dict[str, str], Field(title="Patient Contact", description="Contact information for the patient", json_schema_extra={"example": {"email": "c7c2A@example.com", "phone": "123-456-7890"}})]

    # @computed_field marks this property as a pydantic field that is auto-calculated
    # @property makes it act like an attribute (patient.bmi) instead of a method (patient.bmi())
    # return type hint '-> float' is required by pydantic for computed fields
    @computed_field
    @property
    def bmi(self) -> float:
        # BMI formula: weight (kg) / height (m)^2
        # height is stored in cm so divide by 100 to convert to meters first
        bmi = self.weight / ((self.height / 100) ** 2)
        return round(bmi, 2)   # round to 2 decimal places for clean output

def update_patient_info(patient: Patient):
    print("Patient information updated successfully.")
    print(f"Updated Patient Age: {patient.age}")
    print(f"Patient Name: {patient.name}")
    print(f"Patient Email: {patient.email}")
    print(f"Patient LinkedIn: {patient.LinkedIn}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Height: {patient.height}")
    print(f"Patient BMI: {patient.bmi}")    # bmi is auto-calculated — not passed in the dict
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact: {patient.contact}")

patientinfo: Dict[str, Any] = {
    "name": "John Doe",
    "age": 20,
    "email": "c7c2A@example.com",
    "LinkedIn": "https://www.linkedin.com/in/johndoe",
    "weight": 70.5,
    "height": 175.0,     # height is provided — pydantic uses it to compute bmi automatically
    "married": True,
    "allergies": ["penicillin", "latex"],
    "contact": {"email": "c7c2A@example.com", "phone": "123-456-7890"}
}

patient1 = Patient(**patientinfo)
update_patient_info(patient1)
