from datetime import date
from pydantic import BaseModel


class Consultation(BaseModel):
    consultation_id: int
    client_id: int
    pet_id: int
    consultation_date: date
    description: str
