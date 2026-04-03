from pydantic import BaseModel
class patient(BaseModel):
    name: str
    age: int

def inserted_patient_info(patient: patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print("Patient information inserted successfully.")

def update_patient_info(patient: patient):
    patient.age = 30
    print("Patient information updated successfully.")

patientinfo = {
    "name": "John Doe",
    "age": 25}
patient1 = patient(**patientinfo)
inserted_patient_info(patient1)
