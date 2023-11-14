# repository - работа с БД
from Arcitecture.Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Arcitecture.Seminar_10.clinic.services.clients import ClientService

client_repository = ClientRepository()
# service - слой UseCase
client_service = ClientService(client_repository)


def get_client_service() -> ClientService:
    return client_service
