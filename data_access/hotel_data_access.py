from __future__ import annotations

import model
from model import Hotel
from model import Address

from data_access.base_data_access import BaseDataAccess

from data_access.address_data_access import AddressDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

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
            address_id=address_id,
            stars=stars

        )

    def show_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        if hotel_id is None:
            raise Exception('Hotel ID is required')
        sql = """ 
        SELECT
            HotelId,
            AddressId,
            Name,
            Stars
        FROM Hotel WHERE HotelId = ?
                  """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            (
                hotel_id,
                address_id,
                name,
                stars

            ) = result
            ## Das in eusem model Hotel erwitere no
            return model.Hotel(
                hotel_id,
                address_id,
                name,
                stars
            )
        else:
            return None


    def show_hotels_by_address(self, address: model.Address) -> list[model.Hotel]:
        sql = """
        SELECT
            HotelId,
            AddressID,
            Name,
            Stars
        FROM Hotel WHERE AddressID = ?
        """
        params = tuple([address.address_id])
        hotels = self.fetchall(sql, params)

        return [
            model.Hotel(
                hotel_id,
                name,
                stars

        )
        for(hotel_id,
            address_id,
            name,
            stars

            ) in hotels
        ]




