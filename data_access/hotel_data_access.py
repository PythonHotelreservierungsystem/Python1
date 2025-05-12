import model

from data_access.base_data_access import BaseDataAccess
from model import hotel
## Do stimmt fix no ganz vil nit aber isch trotzdem mol do

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_hotel(self, name: str, stars: int, address: model.Address = None) -> model.Hotel:
        sql = """
        INSERT INTO Hotel(name, stars, address) VALUES (?, ?, ?)
        """
        params = (
            name,
            hotel.hotel_id if hotel else None,
        )

        last_row_id, row_count = self.execute(sql, params)
        return model.Hotel(last_row_id, name, stars, address)





