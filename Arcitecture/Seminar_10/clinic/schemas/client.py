from datetime import date

from pydantic import BaseModel


class Client(BaseModel):
    client_id: int
    document: str
    surname: str
    firstname: str
    patronymic: str
    birthday: date