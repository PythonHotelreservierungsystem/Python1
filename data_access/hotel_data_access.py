from __future__ import annotations

import model

from model import Hotel

from data_access.base_data_access import BaseDataAccess


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
                     address_id:model.Address,
                     stars: int,
                     type: str,
                     is_accessible: bool = True
    ) -> model.Hotel:
        if name is None:
            raise ValueError("Hotel name cannot be None")
        if address_id is None:
            raise ValueError("Hotel address id cannot be None")
        if stars is None:
            raise ValueError("Hotel stars cannot be None")
        if type is None:
            raise ValueError("Hotel type cannot be None")

        sql = """
        INSERT INTO Hotel(Name, Address, Stars, Type, IsAccessible)
        VALUES (?, ?, ?, ?, ?)
        """
        params = tuple([
            name,
            address_id,
            stars,
            type,
            is_accessible
        ])

        last_row_id, row_count = self.execute(sql, params)

        return model.Hotel(
            hotel_id=last_row_id,
            name=name,
            address=address_id,
            stars=stars,
            type=type,
            ## Do müend mir allwe irgendwie no d Buechige integriere
            ## oder das ganze über d Bookings oder halt Room definiere
            is_accessible=is_accessible
        )

    def show_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        if hotel_id is None:
            raise Exception('Hotel ID is required')
        sql = """ 
        SELECT
            HotelId,
            AddressID,
            Name,
            Stars,
            Type, 
            IsAccessible 
        FROM Hotel WHERE HotelId = ?
                  """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            (
                hotel_id,
                address_id,
                name,
                stars,
                type,
                is_accessible
            ) = result
            ## Das in eusem model Hotel erwitere no
            return model.Hotel(
                hotel_id,
                address_id,
                name,
                stars,
                type,
                is_accessible
            )
        else:
            return None


    def show_hotels_by_address(self, address: model.Address) -> list[model.Hotel]:
        sql = """
        SELECT
            HotelId,
            AddressID,
            Name,
            Stars,
            Type,
            IsAccessible
        FROM Hotel WHERE AddressID = ?
        """
        params = tuple([address.address_id])
        hotels = self.fetchall(sql, params)

        return [
            model.Hotel(
                hotel_id,
                name,
                stars,
                type,
                is_accessible,
                address_id=address
        )
        for(hotel_id,
            address_id,
            name,
            stars,
            type,
            is_accessible
            ) in hotels
        ]




