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

if __name__ == "__main__":
    from data_access.room_data_access import RoomDataAccess
    from data_access.facility_data_access import FacilityDataAccess
    from data_access.booking_data_access import BookingDataAccess
    from datetime import datetime

    # DB-Pfad anpassen
    db_path = "../database/hotel_reservation_sample.db"

    # Manager erstellen
    manager = RoomManager(
        room_data_access=RoomDataAccess(db_path),
        facility_data_access=FacilityDataAccess(db_path)
    )
    booking_dao = BookingDataAccess(db_path)

    # Testdaten für Zeitraum
    check_in = datetime(2025, 8, 20)
    check_out = datetime(2025, 8, 22)

    # Methode aufrufen
    verfuegbare_zimmer = manager.find_available_rooms_by_dates(
        check_in_date=check_in,
        check_out_date=check_out,
        booking_dao=booking_dao
    )

    # Ausgabe
    if not verfuegbare_zimmer:
        print("Keine verfügbaren Zimmer im gewünschten Zeitraum.")
    else:
        print(f"Verfügbare Zimmer vom {check_in.date()} bis {check_out.date()}:")
        for room in verfuegbare_zimmer:
            ausstattung = ", ".join([f.facility_name for f in room.facilities])
            print(f"Zimmer {room.room_number} – {room.room_type.description}")
            print(f"  Max. Gäste: {room.room_type.max_guests}")
            print(f"  Preis pro Nacht: {room.price_per_night:.2f} CHF")
            print(f"  Ausstattung: {ausstattung}")
            print("-" * 60)