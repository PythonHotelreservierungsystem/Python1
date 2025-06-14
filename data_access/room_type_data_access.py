import model

from data_access.base_data_access import BaseDataAccess


class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    #Hilfsfunktion
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

    #User Story 10.5
    def update_room_type(self, room_type_id:int, description: str, max_guests: int)-> model.RoomType:
        sql="""
        UPDATE Room_Type SET Description = ?, Max_Guests = ? 
        WHERE Type_Id = ?"""
        params = (description,max_guests,room_type_id)
        _,row_count = self.execute(sql,params)
        return row_count > 0

    #User Story 10.5
    def read_all_room_types(self)->list[model.RoomType]:
        sql="""
        SELECT Type_Id, Description, Max_Guests FROM Room_Type"""
        room_types = self.fetchall(sql)
        return_list = []
        for room_type_id, description, max_guests in room_types:
            return_list.append(model.RoomType(room_type_id, description, max_guests))
        return return_list
