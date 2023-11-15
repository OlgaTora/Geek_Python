from typing import List, Any
from fastapi import APIRouter
from Arcitecture.Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Arcitecture.Seminar_10.clinic.schemas.client import Client
from Arcitecture.Seminar_10.clinic.schemas.client import CreateClientRequest

router = APIRouter()
_client_repo = ClientRepository()


@router.get('/get-all-clients/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Client],
            description='Get all clients', )
async def get_all_clients() -> List[Client]:
    clients = await _client_repo.get_all()
    return clients


@router.post('/create-new-client/',
             responses={400: {'description': 'Bad request'}},
             response_model=Client,
             description='Create client', )
async def create_client(new_client: CreateClientRequest) -> dict[str, Any]:
    result = await _client_repo.create(new_client)
    return result


@router.get('/get-client-by-id/{client_id}', responses={400: {'description': 'Bad request'}},
            response_model=Client,
            description='Search client by id')
async def get_client_by_id(client_id: int) -> Client:
    result = await _client_repo.get_by_id(client_id)
    return result


@router.delete('/delete-client/{client_id}', responses={400: {'description': 'Bad request'}},
               response_model=int,
               description='Delete client by id')
async def delete_client(client_id: int) -> int:
    result = await _client_repo.delete(client_id)
    return result


@router.put('/update-client/{client_id}', responses={400: {'description': 'Bad request'}},
            response_model=int,
            description='Update client by id')
async def update_client(client_id: int, item: Client) -> int:
    result = await _client_repo.update(client_id, item)
    return result
