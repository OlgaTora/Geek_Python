from datetime import date
from typing import List, Any
from fastapi import APIRouter
from Arcitecture.Seminar_10.clinic.repositories.consult_repository import ConsultRepository
from Arcitecture.Seminar_10.clinic.schemas.consultation import Consultation
from Arcitecture.Seminar_10.clinic.schemas.consultation import CreateConsultationRequest

router = APIRouter()
_consult_repo = ConsultRepository()


@router.get('/get-all-consultations/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Consultation],
            description='Get all consultation', )
async def get_all_clients() -> List:
    clients = await _consult_repo.get_all()
    return clients


@router.post('/create-new-consultation/',
             responses={400: {'description': 'Bad request'}},
             response_model=Consultation,
             description='Create consultation', )
async def create_client(new_consultation: CreateConsultationRequest) -> dict[str, Any]:
    result = await _consult_repo.create(new_consultation)
    return result


@router.get('/get-consultation-by-id/{consultation_id}', responses={400: {'description': 'Bad request'}},
            response_model=Consultation,
            description='Search consultation by id')
async def get_client_by_id(consultation_id: int) -> Consultation:
    result = await _consult_repo.get_by_id(consultation_id)
    return result


@router.get('/get-consultation-by-date/{consultation_date}', responses={400: {'description': 'Bad request'}},
            response_model=list[Consultation],
            description='Search consultation by id')
async def get_client_by_id(consultation_date: date) -> list[Consultation]:
    result = await _consult_repo.get_by_date(consultation_date)
    return result


@router.delete('/delete-consultation/{consultation_id}', responses={400: {'description': 'Bad request'}},
               response_model=int,
               description='Delete consultation by id')
async def delete(consultation_id: int) -> int:
    result = await _consult_repo.delete(consultation_id)
    return result


@router.put('/update-consultation/{consultation_id}', responses={400: {'description': 'Bad request'}},
            response_model=int,
            description='Update consultation by id')
async def update(consultation_id: int, item: Consultation) -> int:
    result = await _consult_repo.update(consultation_id, item)
    return result
