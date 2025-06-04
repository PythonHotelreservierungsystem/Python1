import model
from data_access.hotel_data_access import HotelDataAccess


class HotelManager:
    def __init__(self, hotel_data_access: HotelDataAccess):
        self.__hotel_da = hotel_data_access


    ## user Story 1.1
    def show_hotels_by_city(self, city: str) -> list[model.Hotel]:
        #Gibt alle Hotels zurück, deren zugehörige Adresse in der angegebenen Stadt liegt
        alle_hotels = self.__hotel_da.read_all_hotel()
        #nun nur die nach der stadt gesuchten zurückgeben
        return [h for h in alle_hotels if h.address.city == city]

if __name__ == "__main__":
    # 1) DAO instanziieren (Pfad anpassen, falls nötig)
    dao = HotelDataAccess("../database/hotel_reservation_sample.db")
    # 2) Manager mit der DAO erzeugen
    manager = HotelManager(dao)

    # 3) Nach Stadt filtern, z.B. "Berlin"
    stadt = "Berlin"
    hotels_in_berlin = manager.show_hotels_by_city(stadt)

    # 4) Ausgabe
    if not hotels_in_berlin:
        print(f"Keine Hotels in {stadt} gefunden.")
    else:
        print(f"Hotels in {stadt}:")
        for h in hotels_in_berlin:
            print(f"  • {h.name} (ID={h.hotel_id}), {h.address.street}, {h.address.zip_code}")
