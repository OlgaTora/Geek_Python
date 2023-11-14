from fastapi import HTTPException

from Arcitecture.Seminar_10.clinic.database.connections import Connection
from Arcitecture.Seminar_10.clinic.repositories.irepository import IRepository
from Arcitecture.Seminar_10.clinic.schemas.client import Client
# from Arcitecture.Seminar_10.clinic.services.db import database, clients
from Arcitecture.Seminar_10.clinic.services.config import DATABASE_URL


class ClientRepository(IRepository):

    def get_all(self) -> list[Client]:
        sql_script = 'SELECT * FROM Clients'
        connect = Connection(DATABASE_URL).create_connection()
        cursor = connect.cursor()
        cursor.execute(sql_script)
        clients = cursor.fetchall()
        if not clients:
            raise HTTPException(status_code=404, detail="Table 'clients' is empty")
        connect.commit()
        connect.close()
        return clients

    def get_by_id(self, id: int) -> Client:
        pass

    def create(self, client: Client):
        sql_script = 'INSERT INTO Clients VALUES (?, ?, ?, ?, ?, ?)'
        connect = Connection(DATABASE_URL).create_connection()
        cursor = connect.cursor()
        cursor.execute(sql_script,
                       (client.client_id, client.document, client.surName, client.firstName, client.patronymic, client.birthday))
        connect.commit()
        connect.close()
#(client_id, document, surname, firstname, patronymic, birthday)
    def update(self, item: Client):
        pass

    def delete(self, item: Client):
        pass
