import model

from data_access.base_data_access import BaseDataAccess


class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room(
            self,
            room_no: str,
            price_per_night: float,
            room_type: model.RoomType = None,
            hotel_id: model.Hotel = None,
            facility_id: model.Facility = None
    ) -> model.Room:
        if room_no is None:
            raise ValueError("Room number cannot be None")
        if price_per_night is None:
            raise ValueError("Price per night cannot be None")
        if room_type is None:
            raise ValueError("Room type cannot be None")
        sql ="""
        INSERT INTO Room (Room_Number, Price_Per_Night, Type_Id, Hotel_ID)
        VALUES (?, ?, ?, ?)"""

        params = (room_number, price_per_night, Room_Type.room_type_id, Hotel.hotel_id)

        last_row_id, row_count = self.execute(sql, params)

        return model.Room(
            room_id=last_row_id,
            room_no=room_number,
            room_type=room_type_id,
            price_per_night=price_per_night,
            hotel=hotel_id,
            facilities=facility_id
        )
##User Story 2.1
    def show_room_by_details(self, room_type: model.RoomType) -> list[model.Room]:
        sql = """
        SELECT"""



