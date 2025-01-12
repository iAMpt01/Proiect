from pydantic import BaseModel 
from typing import Optional
from datetime import datetime

class PatientData(BaseModel):
    patient_id: int
    heart_rate: int
    temperature: float
    blood_pressure: str
    timestamp: datetime
