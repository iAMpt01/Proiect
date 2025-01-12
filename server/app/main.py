from fastapi import FastAPI
from typing import List
from fastapi import FastAPI
from typing import List
from app.models import PatientData
from app.storage import save_data, get_all_data
from app.sensor import generate_patient_data

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API-ul funcționează corect! Accesează /data sau /sensor pentru mai multe detalii."}


# Definirea unei rute pentru /sensor
@app.get("/sensor")
async def get_sensor_data():
    # Aici poți adăuga logica pentru a prelua datele de la senzor
    return {"sensor_data": "Aceasta este o simulare a datelor senzorului"}


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
