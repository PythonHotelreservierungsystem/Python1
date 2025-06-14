import model
from model import Room
from model import Hotel
from model import RoomType

from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess



class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None, address_data_access: AddressDataAccess = None):
        super().__init__(db_path)
        self.__address_da = AddressDataAccess(db_path)

    # Room erstellen
    def create_room(
            self,
            room_number: int,
            price_per_night: float,
            room_type: model.RoomType = None,
            hotel_id: Hotel = None,
        
    ) -> model.Room:
        if room_number is None:
            raise ValueError("Room number cannot be None")
        if price_per_night is None:
            raise ValueError("Price per night cannot be None")
        if room_type is None:
            raise ValueError("Room type cannot be None")
        sql ="""
        INSERT INTO Room (Room_Number, Price_Per_Night, Type_Id, Hotel_ID)
        VALUES (?, ?, ?, ?)"""

        params = (room_number, price_per_night, RoomType.room_type_id, Hotel.hotel_id)

        last_row_id, row_count = self.execute(sql, params)

        return model.Room(
            room_id=last_row_id,
            room_number=room_number,
            room_type=room_type,
            price_per_night=price_per_night,
            hotel=hotel_id,
            )


    ##User Story 2.1
    def show_room_details(self) -> list[Room]:
        sql = """
              SELECT Room.room_id, room_number, price_per_night,
                     Room_Type.type_id, description, max_guests, Hotel.hotel_id, name, stars, address_id
                FROM Room
                JOIN Room_Type ON Room.type_id = Room_Type.type_id
                JOIN Hotel ON Room.hotel_id = Hotel.hotel_id \
              """
        rooms = self.fetchall(sql)
        return_list = []

        for room_id, room_number, price_per_night, type_id, description, max_guests, hotel_id, name, stars, address_id in rooms:
            #Address-Objekt laden:
            address = self.__address_da.show_address_by_id(address_id)

            #Hotel mit Address-Objekt erstellen:
            hotel = Hotel(hotel_id, name, stars, address)

            #Room mit Hotel + RoomType erstellen:
            room_type = RoomType(type_id, description, max_guests)
            room = Room(room_id, room_number, price_per_night, room_type, hotel)

            return_list.append(room)
        return return_list

    #User Story 10
    def show_room_details_by(self) -> list[model.Room]:
        sql = """SELECT room_id, room_number, price_per_night
        FROM Room """
        rooms= self.fetchall(sql)
        retrun_list = []
        for room_id, room_number, price_per_night in rooms:
            retrun_list.append(Room(room_id, room_number, price_per_night))
        return retrun_list



    def get_rooms_with_facilities(self) -> list[Room]:
        sql = """
              SELECT r.room_id, r.room_number, r.price_per_night, rt.type_id, rt.description, rt.max_guests, h.hotel_id, 
                     h.name, h.stars, h.address_id, f.facility_id, f.facility_name
              FROM Room r
              JOIN Room_Type rt ON r.type_id = rt.type_id
              JOIN Hotel h ON r.hotel_id = h.hotel_id
              LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
              LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
              ORDER BY r.room_id \
              """
        results = self.fetchall(sql)
        rooms_dict = {}

        for row in results:
            (
                room_id, room_number, price_per_night,
                type_id, description, max_guests,
                hotel_id, name, stars, address_id,
                facility_id, facility_name
            ) = row
            if room_id not in rooms_dict:
                address = self.__address_da.show_address_by_id(address_id)
                hotel = Hotel(hotel_id, name, stars, address)
                room_type = RoomType(type_id, description, max_guests)
                room = Room(room_id, room_number, price_per_night, room_type, hotel)
                room.facilities = []
                rooms_dict[room_id] = room
            if facility_id:
                facility = model.Facility(facility_id, facility_name)
                rooms_dict[room_id].facilities.append(facility)
        return list(rooms_dict.values())
    #User Story 10
    def update_room(self, room_id: int, room_number: int, price_per_night: float) -> bool:
        sql="""
        UPDATE Room SET room_number       = ?, price_per_night      = ?
        WHERE room_id = ?"""
        params = (room_number, price_per_night, room_id)
        _, row_count = self.execute(sql, params)
        return row_count > 0

