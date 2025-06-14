from __future__ import annotations

import model
from model import Hotel
from model import Address

from data_access.base_data_access import BaseDataAccess


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    #Alle Hotelinfos aus DB holen
    #User Story 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 10.7
    def read_all_hotel(self,):
        sql = """
        SELECT hotel_id, name, stars, Address.address_id, street, city, zip_code FROM Hotel
        JOIN Address ON hotel.address_id = address.address_id
        """
    # erstellt mit den Hotelinfos hotel und Address & fetchall holt alle Zeilen aus der DB
        hotels = self.fetchall(sql)
        return_list = []
        for hotel_id, name, stars, address_id, street, city, zip_code in hotels:
            return_list.append(Hotel(hotel_id, name, stars, Address(address_id, street, city, int(zip_code))))
        return return_list

    #User Story 3.1
    #Hotel erstellen
    def create_hotel(self,name: str, stars: int, address_id: model.Address) -> model.Hotel:
        if name is None:
            raise ValueError("name cannot be None")
        if stars is None:
            raise ValueError("stars cannot be None")
        sql = """ \
              INSERT INTO Hotel(name, stars, address_id) \
              VALUES (?, ?, ?) \
            """
        params = tuple([name, stars, address_id])
        lastrow_id, row_count = self.execute(sql, params)

        return model.Hotel(
            hotel_id=lastrow_id,
            name=name,
            stars=stars,
            address=address_id
        )

    #User Story 3.2
    def delete_hotel_by_id(self, hotel_id: int) -> bool:
        if hotel_id is None:
            raise ValueError("hotel_id darf nicht None sein")
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        params = (hotel_id,)
        _, row_count = self.execute(sql, params)
        return row_count > 0

    #User Story 3.3, 10.7
    def update_hotel(self, hotel_id: int, name: str, stars: int, address_id: int) -> bool:
        sql = """
              UPDATE Hotel SET name       = ?, stars      = ?, address_id = ? WHERE hotel_id = ? 
              """
        params = (name, stars, address_id, hotel_id)
        _, row_count = self.execute(sql, params)
        return row_count > 0