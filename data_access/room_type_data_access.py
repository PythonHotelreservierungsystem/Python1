import model

from data_access.base_data_access import BaseDataAccess


class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room_type(
            self,
            description: str,
            max_guests: int,
    ) -> model.RoomType:
        if description is None:
            raise ValueError("description cannot be None")
        if max_guests is None:
            raise ValueError("max_guests cannot be None")

        sql ="""
        INSERT INTO Room_Type (Description, Max_Guests)
        VALUES (?, ?)"""

        params =(description, max_guests)

        last_row_id, row_count = self.execute(sql, params)

        return model.RoomType(
            room_type_id=last_row_id,
            description=description,
            max_guests=max_guests
        )
