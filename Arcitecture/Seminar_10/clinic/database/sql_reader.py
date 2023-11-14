import sqlite3

from Arcitecture.Seminar_10.clinic.logger import logger


class SQLReader:
    def __init__(self, connection):
        self.connection = connection

    def execute_sql_script(self, sql_script: str) -> None:
        """Function for execute sql script to table"""
        conn = self.connection.create_connection()
        try:
            cur = conn.cursor()
            cur.execute(sql_script)
            conn.commit()
        except ConnectionError as conn_error:
            logger.info(conn_error)
        except FileNotFoundError as file_error:
            logger.info(file_error)
        except sqlite3.Error as sql_error:
            logger.info(sql_error)
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()
