from __future__ import annotations
from datetime import date
import model
from model import Hotel
from model import Address
import sqlite3
from typing import List


from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = "../database/hotel_reservation_sample.db"):
        super().__init__(db_path)
        self._db_path = db_path  # WICHTIG!

    def show_hotels_by_city(self, city: str) -> list[model.Hotel]:
        sql = """
            SELECT h.hotel_id,
                   h.name,
                   h.address_id,
                   h.stars,
                   a.street,
                   a.city,
                   a.zip_code
            FROM Hotel h
            JOIN Address a ON h.address_id = a.address_id
            WHERE LOWER(a.city) = LOWER(?)
        """
        rows = self.fetchall(sql, (city,))  # nutzt BaseDataAccess-Funktion

        hotels = []
        for row in rows:
            adresse = model.Address(
                address_id=row[2],
                street=row[4],
                city=row[5],
                zip_code=row[6]
            )
            hotel = model.Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[3],
                address=adresse
            )
            hotels.append(hotel)
        return hotels

            
            








