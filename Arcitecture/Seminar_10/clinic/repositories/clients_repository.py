from fastapi import HTTPException

from Arcitecture.Seminar_10.clinic.repositories.irepository import IRepository
from Arcitecture.Seminar_10.clinic.schemas import client
# from Arcitecture.Seminar_10.clinic.services.db import database, clients


class ClientRepository(IRepository):

    async def get_all(self) -> list[client]:
        query = clients.select()
        result = await database.fetch_all(query)
        if not result:
            raise HTTPException(status_code=404, detail="Table 'clients' is empty")
        return result

    def get_by_id(self, id: int) -> client:
        pass

    def create(self):
        pass

    def update(self, item: client):
        pass

    def delete(self, item: client):
        pass
