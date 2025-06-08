import model
from model import Hotel, Room
from data_access import RoomDataAccess, FacilityDataAccess
from data_access import RoomDataAccess
from data_access import HotelDataAccess, BookingDataAccess
from datetime import datetime, date


class RoomManager:
    def __init__(self, room_data_access: RoomDataAccess, facility_data_access: FacilityDataAccess):
        self.__room_da = room_data_access
        self.__facility_da = facility_data_access


        # User Story 2.1 – Zimmerdetails mit Ausstattung
    def show_room_details(self) -> list[Room]:
        rooms = self.__room_da.show_room_details()
        for room in rooms:
            # Hole die Ausstattung zu jedem Zimmer
            room.facilities = self.__facility_da.get_facilities_by_room_id(room.room_id)
        return rooms

        # User Story 2.2
    def find_available_rooms_by_dates(
            self, check_in_date: date, check_out_date: date,
            booking_dao: BookingDataAccess) -> list[Room]:

        # Datum sicherstellen
        if isinstance(check_in_date, datetime):
            check_in_date = check_in_date.date()
        if isinstance(check_out_date, datetime):
            check_out_date = check_out_date.date()

        all_rooms = self.__room_da.show_room_details()
        bookings = booking_dao.show_bookings_with_hotels()
        available_rooms = []
        for room in all_rooms:
            relevant_bookings = [
                b for b in bookings
                if b.room_id == room.room_id and not b.is_cancelled
            ]
            # überschneidung überprüfen
            conflict = any(
                not (check_out_date <= b.check_in_date or check_in_date >= b.check_out_date)
                for b in relevant_bookings
            )
            if not conflict:
                room.facilities = self.__facility_da.get_facilities_by_room_id(room.room_id)
                available_rooms.append(room)
        return available_rooms

