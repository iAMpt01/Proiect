import json
from typing import List
from datetime import datetime
from .models import PatientData

FILE_PATH = "data/patients_data.json"

def save_data(data: PatientData):
    try:
        with open(FILE_PATH, "r") as file:
            patients_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        patients_data = []

    patients_data.append(data.dict())
    
    with open(FILE_PATH, "w") as file:
        json.dump(patients_data, file, default=str, indent=4)

def get_all_data() -> List[PatientData]:
    try:
        with open(FILE_PATH, "r") as file:
            patients_data = json.load(file)
            return [PatientData(**item) for item in patients_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
