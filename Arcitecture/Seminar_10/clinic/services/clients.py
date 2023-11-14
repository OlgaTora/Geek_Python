from typing import List

from Arcitecture.Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Arcitecture.Seminar_10.clinic.schemas.client import Client


class ClientService:
    def __init__(self, repository: ClientRepository) -> None:
        self.repository = repository

    def get_all_clients(self) -> List[Client]:
        result = self.repository.get_all()
        return result

    def get_client_by_id(self, client_id: int) -> Client:
        result = self.repository.get_by_id(client_id)
        return result

    def create_client(self) -> Client:
        result = self.repository.create()
        return result

    def update_client(self, client_id: int) -> Client:
        result = self.repository.update(client_id)
        return result

    def delete_client(self, client_id: int) -> Client:
        result = self.repository.delete(client_id)
        return result
