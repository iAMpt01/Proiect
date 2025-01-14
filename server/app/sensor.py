import random
from datetime import datetime
from .models import HeartHealthData

def generate_heart_health_data(patient_id: int) -> HeartHealthData:
    heart_rate = random.randint(60, 120)  # Pulsul între 60 și 120 bpm
    oxygen_level = round(random.uniform(85, 100), 1)  # Nivelul de oxigen între 85 și 100%
    blood_pressure = f"{random.randint(110, 180)}/{random.randint(70, 120)}"  # Presiune arterială
    timestamp = datetime.now()
    
    health_data = HeartHealthData(
        patient_id=patient_id,
        heart_rate=heart_rate,
        oxygen_level=oxygen_level,
        blood_pressure=blood_pressure,
        timestamp=timestamp,
    )
    
    health_data.detect_condition()  # Detectează afecțiunea, dacă este cazul
    
    return health_data
