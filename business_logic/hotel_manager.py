import model
from data_access.hotel_data_access import HotelDataAccess



class HotelManager:
    def __init__(self, hotel_data_access: HotelDataAccess):
        self.__hotel_da = hotel_data_access


    ## user Story 1.1
    ## user Story 1.1
    def show_hotels_by_city(self, city: str) -> list[model.Hotel]:
        # Gibt alle Hotels zurück, deren zugehörige Adresse in der angegebenen Stadt liegt
        alle_hotels = self.__hotel_da.read_all_hotel()
        # nun nur die nach der stadt gesuchten zurückgeben
        return [h for h in alle_hotels if h.address.city == city]


