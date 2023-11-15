from typing import List, Dict, Any
from fastapi import APIRouter
from Arcitecture.Seminar_10.clinic.repositories.pets_repository import PetRepository
from Arcitecture.Seminar_10.clinic.schemas.pet import Pet
from Arcitecture.Seminar_10.clinic.schemas.pet import CreatePetRequest

router = APIRouter()
_pet_repo = PetRepository()


@router.get('/get-all-pets/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Pet],
            description='Get all pets', )
async def get_all_pets() -> List[Pet]:
    pets = await _pet_repo.get_all()
    return pets


@router.post('/create-new-pet/',
             responses={400: {'description': 'Bad request'}},
             response_model=Pet,
             description='Create client', )
async def create_pet(new_pet: CreatePetRequest) -> dict[str, Any]:
    result = await _pet_repo.create(new_pet)
    return result


@router.get('/get-pet-by-id/{pet_id}', responses={400: {'description': 'Bad request'}},
            response_model=Pet,
            description='Search pet by id')
async def get_pet_by_id(pet_id: int) -> Pet:
    result = await _pet_repo.get_by_id(pet_id)
    return result


@router.get('/get-pet-by-client-id/{client_id}', responses={400: {'description': 'Bad request'}},
            response_model=list[Pet],
            description='Search pet by client id')
async def get_pet_by_id(client_id: int) -> list[Pet]:
    result = await _pet_repo.get_by_client_id(client_id)
    return result


@router.delete('/delete-pet/{pet_id}', responses={400: {'description': 'Bad request'}},
               response_model=int,
               description='Delete pet by id')
async def delete_pet(pet_id: int) -> int:
    result = await _pet_repo.delete(pet_id)
    return result


@router.put('/update-pet/{pet_id}', responses={400: {'description': 'Bad request'}},
            response_model=int,
            description='Update pet by id')
async def update_pet(pet_id: int, item: Pet) -> int:
    result = await _pet_repo.update(pet_id, item)
    return result
