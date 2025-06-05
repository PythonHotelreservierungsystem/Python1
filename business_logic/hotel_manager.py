import model
from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess



class HotelManager:
    def __init__(self, hotel_data_access: HotelDataAccess, room_data_access: RoomDataAccess = None):
        self.__hotel_da = hotel_data_access
        self.__room_da = room_data_access



    ## user Story 1.1
    def show_hotels_by_city(self, city: str) -> list[model.Hotel]:
        # Gibt alle Hotels zurück, deren zugehörige Adresse in der angegebenen Stadt liegt
        alle_hotels = self.__hotel_da.read_all_hotel()
        # nun nur die nach der stadt gesuchten zurückgeben
        return [h for h in alle_hotels if h.address.city == city]


    ## user Story 1.2
    def show_hotels_by_city_and_min_stars(self, city: str, min_stars: int) -> list[model.Hotel]:
        # Alle Hotels aus der Datenbank holen
        alle_hotels = self.__hotel_da.read_all_hotel()

        # Filtern nach Stadt und Sterne
        gefiltert = [
            h for h in alle_hotels
            if (h.address.city == city and h.stars >= min_stars)
        ]
        if not gefiltert:
            print(f"Keine Hotels in '{city}' mit mindestens {min_stars} Sternen gefunden.")
            return []
        return gefiltert

    #     # User Story 1.3
    def find_hotels_by_city_and_guests(self, city: str, guest_count: int) -> list:
        if not self.__room_da:
            raise ValueError("RoomDataAccess wurde nicht initialisiert.")
        # alle hotels laden
        hotels = self.hotel_da.read_all_hotel()
        # Räume mit Typ und Hotel laden
        rooms = self.room_da.show_room_details()

        ergebnis = []
        for hotel in hotels:
            if hotel.address.city.strip().lower() != city.strip().lower():
                continue
            # nun prüfen ob es Zimmer hat was genügend platz hat
            for room in rooms:
                if room.hotel.hotel_id == hotel.hotel_id and room.room_type.max_guests >= guest_count:
                    ergebnis.append(hotel)
                    break
        return ergebnis











