from fastapi import FastAPI
from typing import List
from app.models import HeartHealthData
from app.storage import save_data, get_all_data
from app.sensor import generate_heart_health_data

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API-ul de management al sănătății inimii funcționează corect!"}

# Ruta pentru a obține datele despre senzor
@app.get("/sensor/{patient_id}/data", response_model=HeartHealthData)
def read_sensor_data(patient_id: int):
    # Simulăm citirea datelor de la senzor
    data = generate_heart_health_data(patient_id)
    save_data(data)
    return data

@app.get("/data", response_model=List[HeartHealthData])
def get_patient_data():
    # Returnăm toate datele stocate
    return get_all_data()
