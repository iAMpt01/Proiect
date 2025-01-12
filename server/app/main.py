from fastapi import FastAPI
from typing import List
from fastapi import FastAPI
from typing import List
from app.models import PatientData
from app.storage import save_data, get_all_data
from app.sensor import generate_patient_data

app = FastAPI()

@app.get("/sensor/{patient_id}/data", response_model=PatientData)
def read_sensor_data(patient_id: int):
    # Simulăm citirea de la senzor
    data = generate_patient_data(patient_id)
    save_data(data)
    return data

@app.get("/data", response_model=List[PatientData])
def get_patient_data():
    # Returnăm toate datele stocate
    return get_all_data()

def generate_patient_data(patient_id: int):
    # Simulăm generarea datelor pacientului
    return {"patient_id": patient_id, "temperature": 37.5, "blood_pressure": "120/80"}
