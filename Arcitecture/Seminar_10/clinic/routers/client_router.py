from typing import List
from fastapi import APIRouter  # , Depends
# from Arcitecture.Seminar_10.clinic.services.depends import get_client_service
from Arcitecture.Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Arcitecture.Seminar_10.clinic.schemas.client import Client
# from Arcitecture.Seminar_10.clinic.services.clients import ClientService
from Arcitecture.Seminar_10.clinic.schemas.requests.create_client_request import CreateClientRequest

router = APIRouter()
_client_repo = ClientRepository()

@router.get('/get-all/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Client],
            description='Get all clients', )
async def get_all_clients() -> List[Client]:
    clients = _client_repo.get_all()
    return clients


@router.post('/create/',
             responses={400: {'description': 'Bad request'}},
             response_model=List[Client],
             description='Create client', )
async def create_client(new_client: CreateClientRequest) -> Client:
    client = Client(
        client_id=1,
        document=new_client.document,
        surname=new_client.surname,
        firstname=new_client.firstname,
        patronymic=new_client.patronymic,
        birthday=new_client.birthday,
    )
    return _client_repo.create(client)

#
# @router.get('/get-by-id/')  # , response_model=list[])
# async


# def get_by_id():
#     # list_measures: list = _weather_forecast_holder.get(date_from, date_to)
#     return 'ok'  # list_measures
#
#
# @router.put('/update/')  # , response_model=bool)
# async def update(id: int):
#     # result: bool = _weather_forecast_holder.update(measure_date, temperature_c)
#     return 'ok'
#
#
# @router.delete('/delete/')  # , response_model=bool)
# async def delete(id: int):
#     # result: bool = _weather_forecast_holder.delete(measure_date)
#     return 'ok'  # result
