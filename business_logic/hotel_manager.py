import model
from data_access.hotel_data_access import HotelDataAccess


class HotelManager:
    def __init__(self, db_path: str):
        self.__hotel_da = HotelDataAccess(db_path)


    ## user Story 1.1
    def show_hotels_by_city(self, city: str) -> list[model.Hotel]:
        #Gibt alle Hotels zurück, deren zugehörige Adresse in der angegebenen Stadt liegt
        return self.__hotel_da.show_hotels_by_city(city)


