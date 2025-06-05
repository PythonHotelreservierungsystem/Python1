import model
from data_access import BookingDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess
from datetime import date



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
        hotels = self.__hotel_da.read_all_hotel()
        # Räume mit Typ und Hotel laden
        rooms = self.__room_da.show_room_details()

        ergebnis = []
        for hotel in hotels:
            if hotel.address.city.strip().lower() != city.strip().lower():
                continue
            # nun prüfen ob es Zimmer hat was genügend platz hat
            for room in rooms:
                if room.hotel.hotel_id == hotel.hotel_id and room.room_type.max_guests >= guest_count:
                    ergebnis.append(hotel)
                    break
        if ergebnis:
            return ergebnis
        else:
            print(f"Keine Hotels in '{city}' mit mindestens {guest_count} Gasten gefunden.")
            return []

        # User Story 1.4
    def find_available_hotels_by_city_and_dates(self,
        city: str, check_in_date: date, check_out_date:date,
        booking_dao: BookingDataAccess) -> list[model.Hotel]:

        #alle Datenbank abfragen holen
        hotels = self.__hotel_da.read_all_hotel()
        rooms = self.__room_da.show_room_details()
        bookings = booking_dao.show_bookings_with_hotels()

        #nur hotels in gewünschter Stadt
        stadt_hotels = [h for h in hotels if h.address.city.strip().lower() == city.strip().lower()]

        # schauen ob room verfügbar ist
        def is_room_available(room_id, bookings, check_in_date, check_out_date):
            for b in bookings:
                if b.room_id == room_id and not b.is_cancelled:
                    if not (check_out_date <= b.check_in_date or check_in_date >= b.check_out_date):
                        return False
            return True

        verfuegbare_hotels = []
        for hotel in stadt_hotels:
            for room in rooms:
                if room.hotel.hotel_id == hotel.hotel_id and is_room_available(room.room_id, bookings, check_in_date, check_out_date):
                    verfuegbare_hotels.append(hotel)
                    break
        return verfuegbare_hotels



if __name__ == "__main__":
    from data_access.hotel_data_access import HotelDataAccess
    from data_access.room_data_access import RoomDataAccess
    from data_access.booking_data_access import BookingDataAccess
    from datetime import date

    # Datenbankpfad anpassen, falls nötig
    db_path = "../database/hotel_reservation_sample.db"

    # DataAccess-Objekte erstellen
    hotel_da = HotelDataAccess(db_path)
    room_da = RoomDataAccess(db_path)
    booking_da = BookingDataAccess(db_path)

    # HotelManager initialisieren
    manager = HotelManager(hotel_da, room_da)

    # Beispiel: Suche nach verfügbaren Hotels in Basel vom 10.06.2025 bis 12.06.2025
    city = "Genève"
    check_in = date(2025, 7, 10)
    check_out = date(2025, 7, 15)

    result = manager.find_available_hotels_by_city_and_dates(city, check_in, check_out, booking_da)

    # Ausgabe
    if result:
        print(f"Verfügbare Hotels in '{city}' vom {check_in} bis {check_out}:")
        for h in result:
            print(f"  • {h.name} – {h.address.street}, {h.address.zip_code}")
    else:
        print(f"Keine verfügbaren Hotels in '{city}' vom {check_in} bis {check_out}.")












