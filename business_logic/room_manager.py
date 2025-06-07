import model
from model import Hotel, Room
from data_access import RoomDataAccess, FacilityDataAccess
from data_access import RoomDataAccess
from data_access import HotelDataAccess


class RoomManager:
    def __init__(self, room_data_access: RoomDataAccess, facility_data_access: FacilityDataAccess):
        self.__room_da = room_data_access
        self.__facility_da = facility_data_access

        # User Story 2.1 – Raumdetails inkl. Ausstattung

        # User Story 2.1 – Zimmerdetails mit Ausstattung
    def show_room_details(self) -> list[Room]:
        rooms = self.__room_da.show_room_details()
        for room in rooms:
            # Hole die Ausstattung zu jedem Zimmer
            room.facilities = self.__facility_da.get_facilities_by_room_id(room.room_id)
        return rooms

if __name__ == "__main__":
    from data_access.room_data_access import RoomDataAccess
    from data_access.facility_data_access import FacilityDataAccess

    db_path = "../database/hotel_reservation_sample.db"

    manager = RoomManager(
        room_data_access=RoomDataAccess(db_path),
        facility_data_access=FacilityDataAccess(db_path)
    )

    rooms = manager.show_room_details()
    for room in rooms:
        ausstattung = ", ".join([f.facility_name for f in room.facilities])
        print(f"Zimmer {room.room_number} – {room.room_type.description}")
        print(f"  Max. Gäste: {room.room_type.max_guests}")
        print(f"  Preis pro Nacht: {room.price_per_night:.2f} CHF")
        print(f"  Ausstattung: {ausstattung}")
        print("-" * 60)