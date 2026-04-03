from pydantic import BaseModel
from typing import List,Dict
class patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact: Dict[str, str]

def update_patient_info(patient: patient):
    print("Patient information updated successfully.")
    print(f"Updated Patient Age: {patient.age}")
    print(f"Patient Name: {patient.name}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact: {patient.contact}")

patientinfo = {
    "name": "John Doe",
    "age": 20,
    "weight": 70.5,
    "married": True,
    "allergies": ["penicillin", "latex"],
    "contact": {"email": "c7c2A@example.com", "phone": "123-456-7890"}
}
patient1 = patient(**patientinfo)
update_patient_info(patient1)