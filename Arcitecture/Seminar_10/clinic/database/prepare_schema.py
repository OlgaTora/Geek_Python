from Arcitecture.Seminar_10.clinic.database.connections import Connection
from Arcitecture.Seminar_10.clinic.database.sql_reader import SQLReader
from Arcitecture.Seminar_10.clinic.services.config import DATABASE_URL


class PrepareDatabase:

    def prepare_db(self):
        self.prepare_clients()

    @staticmethod
    def prepare_clients():
        connect = Connection(DATABASE_URL)
        reader = SQLReader(connect)
        clients_script = "CREATE TABLE if not EXISTS Clients(" \
                         "ClientId INTEGER PRIMARY KEY," \
                         " Document TEXT, SurName TEXT," \
                         " FirstName TEXT," \
                         " Patronymic TEXT," \
                         " Birthday TEXT);"
        reader.execute_sql_script(clients_script)

#             sqliteCommand.ExecuteNonQuery();
#             sqliteCommand.CommandText =
#                     @"CREATE TABLE Pets(PetId INTEGER PRIMARY KEY,
#                     ClientId INTEGER,
#                     Name TEXT,
#                     Birthday INTEGER)";
#             sqliteCommand.ExecuteNonQuery();
#             sqliteCommand.CommandText =
#                 @"CREATE TABLE Consultations(ConsultationId INTEGER PRIMARY KEY,
#                     ClientId INTEGER,
#                     PetId INTEGER,
#                     ConsultationDate INTEGER,
#                     Description TEXT)";
#             sqliteCommand.ExecuteNonQuery();
#             sqliteCommand.Dispose();
#
