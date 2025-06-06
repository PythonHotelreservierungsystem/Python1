import model
from model import Hotel
from data_access import RoomDataAccess, FacilityDataAccess
from data_access import RoomDataAccess
from data_access import HotelDataAccess

class RoomManager:
    def __init__(self, room_data_access: RoomDataAccess, facility_data_access: FacilityDataAccess):
        self.__room_da = room_data_access
        self.__facility_da = facility_data_access


    def show_rooms(self, name: str) -> list[model.Room]:
        alle_rooms = self.__room_da.show_room_details()
        room_facilities= self.__facility_da

        return[r for r in alle_rooms if r.hotel.name == name]

if __name__ == "__main__":
    dao = RoomDataAccess("../database/hotel_reservation_sample.db")
    manager = RoomManager(dao)

    # nach Stadt filtern im String
    room_nach_x = manager.show_rooms("Hotel Baur au Lac")

    if not room_nach_x :
        print("Keine Zimmer gefunden.")
    else:
        for r in room_nach_x :
            print(f"{r.room_id} – Zimmernummer: {r.room_no}, Zimmerbeschreibung: {r.room_type.description}, PreisproNacht: {r.price_per_night}, MaxGäste: {r.room_type.max_guests}")