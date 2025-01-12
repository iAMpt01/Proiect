import random
from datetime import datetime
from .models import PatientData

def generate_patient_data(patient_id: int) -> PatientData:
    heart_rate = random.randint(60, 100)
    temperature = round(random.uniform(36.5, 39.0), 1)
    blood_pressure = f"{random.randint(110, 130)}/{random.randint(70, 90)}"
    timestamp = datetime.now()
    
    return PatientData(
        patient_id=patient_id,
        heart_rate=heart_rate,
        temperature=temperature,
        blood_pressure=blood_pressure,
        timestamp=timestamp
    )
