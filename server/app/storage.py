import json
from typing import List
from .models import HeartHealthData

FILE_PATH = "data/heart_health_data.json"

def save_data(data: HeartHealthData):
    try:
        with open(FILE_PATH, "r") as file:
            health_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        health_data = []

    health_data.append(data.dict())
    
    with open(FILE_PATH, "w") as file:
        json.dump(health_data, file, default=str, indent=4)

def get_all_data() -> List[HeartHealthData]:
    try:
        with open(FILE_PATH, "r") as file:
            health_data = json.load(file)
            return [HeartHealthData(**item) for item in health_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
