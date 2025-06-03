import os

import sqlite3
from datetime import date, datetime
class BaseDataAccess:
    def __init__(self, connection_str: str = "../../database/hotel_reservation_sample.db"):
        if connection_str:
         self.__connection_str = connection_str
        else:
         self.__connection_str = os.environ.get("../../database/hotel_reservation_sample.db")
         if self.__connection_str is None:
                raise Exception("DB_FILE environment variable or parameter connection_str has to be set.")

    def _connect(self):
        # Mit detect_types=sqlite3.PARSE_DECLTYPES wird
        # der Verbindung gesagt die registrierten Adapter und Konverter zu verwenden
        return sqlite3.connect(self.__connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple = None):
        if params is None:
            # leeres tuple für sql parameter wenn params None ist
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                result = cursor.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
        return result

    def fetchall(self, sql: str, params: tuple = None):
        if params is None:
            # leeres tuple für sql parameter wenn params None ist
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                results = cursor.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
        return results

    def execute(self, sql: str, params: tuple = None):
        if params is None:
            # leeres tuple für sql parameter wenn params None ist
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()
        return cursor.lastrowid, cursor.rowcount
