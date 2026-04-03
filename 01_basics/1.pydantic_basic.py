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
    print(f"Updated Patient Age: {patient.age}")
    print(f"Patient Name: {patient.name}")

patientinfo = {
    "name": "John Doe",
    "age": 20}
patient1 = patient(**patientinfo)
update_patient_info(patient1)

