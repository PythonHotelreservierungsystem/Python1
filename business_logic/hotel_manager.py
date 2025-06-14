from datetime import date, datetime

import model

from data_access.booking_data_access import BookingDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.address_data_access import AddressDataAccess


class HotelManager:
    def __init__(self, hotel_data_access: HotelDataAccess, room_data_access: RoomDataAccess = None, address_data_access: AddressDataAccess = None):
        self.__hotel_da = hotel_data_access
        self.__room_da = room_data_access

    #eifach zum alli Hotels usgeh
    def show_all_hotels_basic(self) -> list[model.Hotel]:
        return self.__hotel_da.read_all_hotel()

    # User Story 3.1
    def create_new_hotel(self, name: str, stars: int, address: model.Address, address_da: AddressDataAccess) -> model.Hotel:
        neues_hotel  = self.__hotel_da.create_hotel(name=name, stars=stars, address_id=address.address_id)
        neue_addresse = address_da.create_address(city=address.city, street=address.street, zip_code=address.zip_code)
        neues_hotel.address = (
            neue_addresse)

        return neues_hotel

    #User Story 3.2
    def update_a_hotel(self, name:str, stars:int, address:model.Address, hotel_id:int, address_da:AddressDataAccess) -> model.Hotel:
        aktualisiertes_hotel=self.__hotel_da.update_hotel(name=name, stars=stars, address_id=address.address_id, hotel_id=hotel_id)
        aktualisiertes_hotel.address=address_da.update_address(address_id=address.address_id, city=address.city, street=address.street, zip_code=address.zip_code)

        return aktualisiertes_hotel


# if __name__ == "__main__":
#     from data_access.hotel_data_access import HotelDataAccess
#     from data_access.booking_data_access import BookingDataAccess
#     from data_access.address_data_access import AddressDataAccess
#     from datetime import datetime
#     from model import Address
#
#     hotel_dao = HotelDataAccess("../database/hotel_reservation_sample.db")
#     address_dao = AddressDataAccess("../database/hotel_reservation_sample.db")
#     manager = HotelManager(hotel_data_access=hotel_dao, address_data_access=address_dao)
#
#     new_address = Address(street="Bundesplatz 5", city="Aarburg", zip_code=3028,)
#     new_hotel = manager.create_new_hotel(name="Hotel Aarhof", stars=5, address=new_address,address_da=address_dao)
#
#     if new_hotel:
#         print("✅ Neues Hotel erfolgreich erstellt:\n")
#         print(f"🏨 Name     : {new_hotel.name}")
#         print(f"⭐ Sterne   : {new_hotel.stars}")
#         print(f"📍 Adresse : {new_hotel.address.street}, {new_hotel.address.zip_code} {new_hotel.address.city}")
#         print(f"🆔 Hotel-ID: {new_hotel.hotel_id}")
#         print(f"🏠 Addr-ID : {new_hotel.address.address_id}")
#     else:
#         print("❌ Hotel konnte nicht erstellt werden.")
#



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


        # User Story 1.3
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
    city: str, check_in_date: date, check_out_date: date,
    booking_dao: BookingDataAccess) -> list[model.Hotel]:

        if isinstance(check_in_date, datetime):
            check_in_date = check_in_date.date()
        if isinstance(check_out_date, datetime):
            check_out_date = check_out_date.date()

        hotels = self.__hotel_da.read_all_hotel()
        rooms = self.__room_da.show_room_details()
        bookings = booking_dao.show_bookings_with_hotels()

        stadt_hotels = [h for h in hotels if h.address.city.strip().lower() == city.strip().lower()]
        verfuegbare_hotels = []

        for hotel in stadt_hotels:
            hotel_rooms = [r for r in rooms if r.hotel.hotel_id == hotel.hotel_id]

            for room in hotel_rooms:
                relevant_bookings = [b for b in bookings if b.room_id == room.room_id and not b.is_cancelled]

                conflict = False
                for b in relevant_bookings:
                    if not (check_out_date <= b.check_in_date or check_in_date >= b.check_out_date):
                        conflict = True
                        break

                if not conflict:
                    if hotel not in verfuegbare_hotels:
                        verfuegbare_hotels.append(hotel)
                    break  # Ein verfügbares Zimmer reicht

        return verfuegbare_hotels

    # User Story 1.5
    def find_hotels_by_criteria(
            self, city: str, check_in_date: date, check_out_date: date, min_stars: int,
            guest_count: int, booking_da: BookingDataAccess) -> list[model.Hotel]:

        # damit date auch wirklich als daze übergeben wird
        if isinstance(check_in_date, datetime):
            check_in_date = check_in_date.date()
        if isinstance(check_out_date, datetime):
            check_out_date = check_out_date.date()

        # daten aus db holen
        hotels = self.__hotel_da.read_all_hotel()
        rooms = self.__room_da.show_room_details()
        bookings = booking_da.show_bookings_with_hotels()

        # Hotels in Wunschstadt und mit min. sternen
        stadt_hotels = [
            h for h in hotels
            if h.address.city.strip().lower() == city.strip().lower() and h.stars >= min_stars
        ]
        verfuegbare_hotels = []

        # alle passende hotel prüfen
        for hotel in stadt_hotels:
            # Alle Zimmer dieses Hotels
            hotel_rooms = [r for r in rooms if r.hotel.hotel_id == hotel.hotel_id]

            for room in hotel_rooms:
                # Prüfen, ob das Zimmer genug Gäste aufnehmen kann
                if room.room_type.max_guests < guest_count:
                    continue  # Zimmer überspringen wenns zu klein ist

                # alle buchungen zum zimmer die nicht storniert wurden
                relevant_bookings = [
                    b for b in bookings
                    if b.room_id == room.room_id and not b.is_cancelled
                ]

                # prüfen ob es  terminüberschneidungen gibt
                conflict = False
                for b in relevant_bookings:
                    if not (check_out_date <= b.check_in_date or check_in_date >= b.check_out_date):
                        conflict = True  # Überschneidung gefunden
                        break

                if not conflict:
                    # Sobald ein Zimmer passt, reicht das – Hotel als verfügbar merken
                    if hotel not in verfuegbare_hotels:
                        verfuegbare_hotels.append(hotel)
                    break  # keine weiteren Zimmer prüfen nötig

        return verfuegbare_hotels

    # User Story 1.6
    def show_all_hotel_infos(self) -> list[str]:
        hotels = self.__hotel_da.read_all_hotel()
        zusammenfassungen = []

        for h in hotels:
            eintrag = f"{h.name} – {h.address.street}, {h.address.zip_code} {h.address.city} ({h.stars} Sterne)"
            zusammenfassungen.append(eintrag)

        return zusammenfassungen

    #Create Hotel User story 3.1
    def create_new_hotel(self, name: str, stars: int, address: model.Address,
                         address_da: AddressDataAccess) -> model.Hotel:
        # 1. Adresse erstellen
        neue_addresse = address_da.create_address(
            street=address.street,
            city=address.city,
            zip_code=address.zip_code
        )
        # 2. Hotel mit der erstellten address id speichern
        neues_hotel = self.__hotel_da.create_hotel(
            name=name,
            stars=stars,
            address_id=neue_addresse.address_id
        )
        # 3. Adresse dem neuuen hotel zuweisen
        neues_hotel.address = neue_addresse

        return neues_hotel

    #delete hotel für user story 3.2
    def delete_hotel(self, hotel_id: int) -> bool:
        return self.__hotel_da.delete_hotel_by_id(hotel_id)


    # Update Hotel für usser story 3.3
    def update_hotel_and_address(
            self,hotel_id: int,name: str,stars: int,address: model.Address,address_da: AddressDataAccess) -> bool:
        # Adresse aktualisieren
        adresse_ok = address_da.update_address(
            address_id=address.address_id,
            street=address.street,
            city=address.city,
            zip_code=address.zip_code
        )
        # Hotel aktualisieren
        hotel_ok = self.__hotel_da.update_hotel(
            hotel_id=hotel_id,
            name=name,
            stars=stars,
            address_id=address.address_id
        )
        return adresse_ok and hotel_ok







