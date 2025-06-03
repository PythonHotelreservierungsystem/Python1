from __future__ import annotations
from datetime import date
import model
from model import Hotel
from model import Address
import sqlite3


from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__("../database/hotel_reservation_sample.db")

    ## def create_new_hotel(self, name: str, stars: int, address: model.Address = None) -> model.Hotel:
    ##    sql = """
    ##    INSERT INTO Hotel(name, stars, address) VALUES (?, ?, ?)
    ##    """
    ##    params = (
    ##        name,
    ##        hotel.hotel_id if hotel else None,
    ##    )

    ##    last_row_id, row_count = self.execute(sql, params)
    ##    return model.Hotel(last_row_id, name, stars, address)
    def create_hotel(self,
                     name: str,
                     stars: int,
                     address_id: model.Address = None
    ) -> model.Hotel:
        if name is None:
            raise ValueError("Hotel name cannot be None")
        ## if address_id is None:
            ##raise ValueError("Hotel address id cannot be None")
        if stars is None:
            raise ValueError("Hotel stars cannot be None")

        sql = """
        INSERT INTO Hotel(Name, Address_Id, Stars)
        VALUES (?, ?, ?)
        """
        params = tuple([
            name,
            Address.address_id if address_id else None,
            stars

        ])

        last_row_id, row_count = self.execute(sql, params)

        return model.Hotel(
            hotel_id=last_row_id,
            name=name,
            address=address_id,
            stars=stars

        )

    def show_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        if hotel_id is None:
            raise Exception('Hotel ID is required')
        sql = """ 
        SELECT
            Hotel_Id,
            Name,
            Address_Id,
            Stars
        FROM Hotel WHERE Hotel_Id = ?
                  """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            (
                hotel_id,
                name,
                address_id,
                stars

            ) = result
            ## Das in eusem model Hotel erwitere no
            return model.Hotel(
                hotel_id,
                name,
                address_id,
                stars
            )
        else:
            return None

    ##User Story 1.1
    ##Gibt alle Hotels zurück, deren zugehörige Adresse in der angegebenen Stadt liegt.
    def show_hotels_by_city(self, city: str) -> list[model.Hotel]:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        sql = """
            SELECT
            h.hotel_id AS hotel_id,
            h.name AS hotel_name,
            h.stars AS hotel_stars,
            a.address_id AS address_id,
            a.street AS street,
            a.city AS city,
            a.zip_code AS zip_code,
        FROM Hotel AS h
        JOIN Address AS a
        ON a.address_id = h.address_id
        WHERE a.city = ?
            """
        cur.execute(sql, (city,))
        rows = cur.fetchall()
        conn.close()
        hotels = list[model.Hotel] = []
        for row in rows:
            adresse = model.Address(
                address_id=row["address_id"],
                street=row["street"],
                city=row["city"],
                zip_code=row["zip_code"]
            )
            hotel = model.Hotel(
                hotel_id=row["hotel_id"],
                name=row["hotel_name"],
                stars=row["hotel_stars"],
                address=adresse
            )
            hotels.append(hotel)
        return hotels


            
            








