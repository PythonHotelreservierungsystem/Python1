import model
from data_access.base_data_access import BaseDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.room_type_data_access import RoomTypeDataAccess
from data_access.address_data_access import AddressDataAccess
from data_access.guest_data_access import GuestDataAccess
from model import Room
from model import Address
from model import Guest
from model import Booking
from model import Guest
from model import Facility
from model import Hotel
from model import RoomType

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
    def read_all_rooms(self,):
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
    def show_room_details(self) -> list[Room]:
        sql = """
        SELECT Room.room_id, room_number, price_per_night, 
        Room_Type.type_id, description, max_guests, 
        Hotel.hotel_id, name, stars, address_id,
        Facilities.facility_id, facility_name
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Facilities ON Room.room_id = Room_Facilities.room_id
        JOIN Facilities ON Room_Facilities.facility_id = Facilities.facility_id
        """

        rooms = self.fetchall(sql)
        return_list = []
        for room_id, room_number, price_per_night, type_id, description, max_guests, hotel_id, name, stars, address_id, facility_name, facility_id in rooms:
            return_list.append(
                Room(
                    room_id=room_id,
                    room_no=room_number,
                    price_per_night=price_per_night,
                    room_type=RoomType(type_id, description, max_guests),
                    hotel=Hotel(hotel_id, name, stars, address_id),
                    facilities=Facility(facility_id, facility_name)
                    )
                )
        return return_list

if __name__ == "__main__":
    # 1) Instanz erzeugen (Pfad anpassen, falls nötig)
    dao = RoomDataAccess("../database/hotel_reservation_sample.db")

    # 2) dao.read_all_hotel() aufrufen und Ergebnis ausgeben
    alle_rooms = dao.show_room_details()
    for r in alle_rooms:
        print(
            f"ID: {r.room_id}, Zimmernummer: {r.room_no}, PreisproNacht: {r.price_per_night}, "
            f"A:{r.room_type.description}, B:{r.room_type.max_guests}, C:{r.hotel.name}, D:{r.hotel.stars}, E:{r.hotel.address}, F:{r.facilities.facility_id}, G:{r.facilities.facility_name}")
## User
##für User story 3.8
    ##def get_bookings_for_rooms(self, room_id: int)-> list[Booking]:
     ##   sql="""
       ## SELECT room_id, guest_id, check_in_date, check_out_date, booking_id
        ##FROM Booking WHERE room_id = ?
        ##"""
       ## params = tuple([room_id])
        ##booking = self.fetchall(sql, params)
        ##return [
           ## model.Booking(
             ##   room_id,
               ## guest,
                ##heck_in_date,
                ##check_out_date,
                ##rooms
            ##)
            ##for(room_id,
              ##  guest,
                ##check_in_date,
                ##check_out_date,
                ##rooms
                ##)in booking
       ## ]
    ##def get_all_with_room_and_hotels(self) -> list[Booking]:
       ## sql="""
        ##SELECT booking.booking_id, booking.room_id, booking.guest_id,
            ##booking.check_in_date, booking.check_out_date, booking.is_cancelled,
           ## booking.total_amount, room.room_number, hotel.hotel_id, hotel.name,
           # hotel.address_id
       # FROM Booking AS booking
        #JOIN Room AS room ON booking.room_id = room.room_id
       #JOIN Hotel AS hotel ON room.hotel_id = hotel.hotel_id
        #"""
       # params = tuple([bookings])
        #result = self.fetchall(sql, params)

        #for results in result:
          #  (
            #    booking_id, room_id, guest_id,
              #  check_in_date, check_out_date,
               # is_cancelled, total_amount, room_number,
               # hotel_id, name, address_id) = results

           # hotel = model.Hotel(
            #    hotel_id=hotel_id,
            #    name=name,
              #  address=hotel_address_id)

           # room = model.Room(
           #     room_id=room_id,
            #    room_no=room_number,
            #    price_per_night=price_per_night,
            #    room_type=room_type_id,
             #   hotel=hotel_id
           # )
           # booking = model.Booking(
           #     booking_id=booking_id,
           #     room_id=room_id,
           #     guest=guest_id,
           #     check_in_date=check_in_date,
           #     check_out_date=check_out_date,
           #     is_cancelled=is_cancelled,
           #     total_amount=total_amount
           # )
           # bookings.append(booking)
           # return bookings


