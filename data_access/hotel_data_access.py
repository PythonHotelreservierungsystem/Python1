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
        SELECT hotel_id, name, stars, Address.address_id, street, city, zip_code FROM Hotel
        JOIN Address ON hotel.address_id = address.address_id
        """
    # erstellt mit den Hotelinfos hotel und Address & fetchall holt alle Zeilen aus der DB
        hotels = self.fetchall(sql)
        return_list = []
        for hotel_id, name, stars, address_id, street, city, zip_code in hotels:
            return_list.append(Hotel(hotel_id, name, stars, Address(address_id, street, city, zip_code)))
        return return_list







