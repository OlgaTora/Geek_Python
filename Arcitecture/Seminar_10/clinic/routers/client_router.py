from starlette.responses import RedirectResponse

from Arcitecture.Seminar_10.clinic.main import app

from typing import List
from fastapi import APIRouter, Depends
from Arcitecture.Seminar_10.clinic.services.depends import get_client_service
from Arcitecture.Seminar_10.clinic.schemas.client import Client
from Arcitecture.Seminar_10.clinic.services.clients import ClientService

router = APIRouter()


@router.get('/get-all/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Client],
            description='Get all clients', )
async def get_all_books(client_service: ClientService = Depends(get_client_service)) -> List[Client]:
    clients = client_service.get_all_clients()
    return clients

@router.post('/create/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Client],
            description='Create client', )
async def create_client(client_service: ClientService = Depends(get_client_service)) -> Client:
    client = client_service.create_client()
    return client

@app.get('/get-by-id/')  # , response_model=list[])
async def get_by_id():
    # list_measures: list = _weather_forecast_holder.get(date_from, date_to)
    return 'ok'  # list_measures


@app.put('/update/')  # , response_model=bool)
async def update(id: int):
    # result: bool = _weather_forecast_holder.update(measure_date, temperature_c)
    return 'ok'


@app.delete('/delete/')  # , response_model=bool)
async def delete(id: int):
    # result: bool = _weather_forecast_holder.delete(measure_date)
    return 'ok'  # result
