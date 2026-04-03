# ============================================================
# FILE: 8.pydantic_Serialization.py
# TOPIC: model serialization — converting models to dicts and JSON
# ============================================================

# model_dump() converts a Pydantic model to a Python dictionary
# model_dump_json() converts a Pydantic model directly to a JSON string
# Both methods support include/exclude to control which fields are serialized
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Annotated, Optional, Any

class Address(BaseModel):
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

# model_dump() converts the model to a Python dictionary
# include parameter — only serialize specified fields
temp1 = patient1.model_dump(include={"name", "age", "email", "LinkedIn", "weight", "married", "allergies", "contact"})

# include with nested model — serialize specific nested fields (exclude address.city)
temp2 = patient1.model_dump(include={"address": {"street", "zip_code"}})

# exclude parameter — serialize all fields except the specified ones
temp3 = patient1.model_dump(exclude={"age", "email", "LinkedIn", "weight", "married", "allergies", "contact"})

# model_dump_json() converts the model directly to a JSON string
temp4 = patient1.model_dump_json()

print('temp1:', temp1)
print('temp2:', temp2)
print('temp3:', temp3)
print('temp4:', temp4)

# Type checking — verify what types are returned by each method
print('Type of temp1:', type(temp1))  # dict
print('Type of temp2:', type(temp2))  # dict
print('Type of temp3:', type(temp3))  # dict
print('Type of temp4:', type(temp4))  # str (JSON string)
