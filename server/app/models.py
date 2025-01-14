from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HeartHealthData(BaseModel):
    patient_id: int
    heart_rate: int  # Pulsul
    oxygen_level: float  # Nivelul de oxigen
    blood_pressure: str  # Presiunea arterială
    ecg: Optional[str] = None  # ECG - opțional, dacă senzorul poate captura acest lucru
    timestamp: datetime
    condition_detected: Optional[str] = None  # Afișează dacă s-a detectat o afecțiune

    # Metoda pentru detectarea afecțiunii (exemplu simplificat)
    def detect_condition(self):
        if self.heart_rate > 100:  # Puls prea mare
            self.condition_detected = "Tachicardie"
        elif self.oxygen_level < 90:  # Nivel oxigen prea scăzut
            self.condition_detected = "Hipoxie"
        elif int(self.blood_pressure.split('/')[0]) > 140:  # Presiune arterială ridicată
            self.condition_detected = "Hipertensiune"
        else:
            self.condition_detected = "Normal"
