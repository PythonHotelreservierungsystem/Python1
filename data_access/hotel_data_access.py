from __future__ import annotations

import model
from model import Hotel
from model import Address

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
    def show_hotels_by_address(self, address: model.Address) -> list[model.Hotel]:
        sql = """
        SELECT
            Hotel_Id,
            Address_Id,
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
    ##User Story 1.2 allwe au nit korrekt falls Fehler in BL
    def show_hotels_by_stars(self, stars: int) -> list[model.Hotel]:
        sql = """
        SELECT
            Hotel_Id,
            Address_Id,
            Name,
            Stars
        FROM Hotel WHERE Stars >= ?
        """
        params = tuple([stars.Hotel])
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
## für UserStory 1.3
    def show_hotel_by_capacity(self, max_guests: model.RoomType) -> list[model.Hotel]:
        sql="""
        SELECT Hotel.Hotel_Id, Hotel.Name, Address.City
        FROM Hotel
        JOIN Address ON Address.Address_Id = Hotel.Address_Id
        WHERE Address.City = ?
            AND EXISTS (
                SELECT 1
                FROM Room
                JOIN RoomType ON RoomType.Room_Type_Id = Room.Room_Type_Id
                WHERE Room.Hotel_Id = Hotel.Hotel_Id
                    AND RoomType.Capacity <= ?)
                    """
        params = tuple([max_guests.room_type_id])
        hotels = self.fetchall(sql, params)
        ###Do sind allwe Fehler falls es bi BL het
        return [
            model.Hotel(
                hotel_id,
                name,
                city,
                max_guests
            )
            for(hotel_id,
                name,
                city,
                max_guests
                ) in hotels
        ]
    ##User Story 3.8
    def get_bookings_for_hotels(self, hotel_id: int)-> list[Booking]:
        sql="""
        SELECT hotel_id, guest, check_in, check_out, rooms
        FROM Booking WHERE hotel_id = ?
        """
        params = tuple([hotel_id])
        booking = self.fetchall(sql, params)
        return [
            model.Booking(
                hotel_id,
                guest,
                check_in,
                check_out,
                rooms
            )
            for(hotel_id,
                guest,
                check_in,
                check_out,
                rooms
                )in booking
        ]


