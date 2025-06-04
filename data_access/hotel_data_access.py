from __future__ import annotations
from datetime import date
import model
from model import Hotel, Address
import sqlite3
from typing import List
from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    #Hotel erstellen
    def create_hotel(self,):
        pass

    #Alle Hotelinfos aus DB holen
    def read_all_hotel(self,):
        sql = """
        SELECT hotel_id, name, stars, Address.address_id, street, city, zip_code FROM hotel
        JOIN Address ON hotel.address_id = address.address_id
        """

        hotels = self.fetchall(sql)
        return_list = []
        for hotel_id, name, stars, address_id, street, city, zip_code in hotels:
            return_list.append(Hotel(hotel_id, name, stars, Address(address_id, street, city, zip_code)))
        return return_list

if __name__ == "__main__":
    # 1) Instanz erzeugen (Pfad anpassen, falls nötig)
    dao = HotelDataAccess("../database/hotel_reservation_sample.db")

    # 2) dao.read_all_hotel() aufrufen und Ergebnis ausgeben
    alle_hotels = dao.read_all_hotel()
    for h in alle_hotels:
        print(
            f"ID: {h.hotel_id}, Name: {h.name}, Sterne: {h.stars}, "
            f"{h.address.street}, {h.address.city} {h.address.zip_code}"
        )






