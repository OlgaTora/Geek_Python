from datetime import date
from pydantic import BaseModel


class Pet(BaseModel):
    pet_id: int
    client_id: int
    name: str
    birthday: date
