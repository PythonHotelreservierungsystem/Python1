from __future__ import annotations

import model

from model import Hotel

from data_access.base_data_access import BaseDataAccess

## Do stimmt fix no ganz vil nit aber isch trotzdem mol do

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

    def show_hotels_by_city(self, city: str) -> model.Hotel:
        if city is None:
            raise ValueError("city cannot be None")

        sql = """
        SELECT City, Name FROM Hotel WHERE City = ? """
        params = tuple([city])
        result = self.fetchall(sql, params)
        if result:
            city = result
            return model.Hotel(city=city, name=Hotel.name)
        else:
            return None


    def show_hotels_by_stars(self, stars: int) -> model.Hotel:
        if stars is None:
            raise ValueError("stars cannot be None")

        sql = """
        SELECT City, Name FROM Hotel WHERE Stars = ?
         """
        params = tuple([stars])
        result = self.fetchall(sql, params)
        if result:
            stars, name = result
            return model.Hotel(stars=stars, name=Hotel.name)
        else:
            return None


