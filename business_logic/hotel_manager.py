import model
import data_access

from data_access import HotelDataAccess


class HotelManager:
    def __init__(self, hotel_id):
        self.__hotel_da = data_access.HotelDataAccess()

    def create_hotel(self,
                     name: str,
                     stars: int,
                     address_id: model.Address = None
                     ) -> model.Hotel:
        return self.__hotel_da.create_hotel(
            name=name,
            stars=stars,
            address_id=address_id
        )

    def show_hotels(self, hotel_id: int) -> model.Hotel:
        return self.__hotel_da.show_hotel_by_id(hotel_id)

hm = HotelManager(HotelDataAccess("../../database/hotel_reservation_sample.db"))
tesst = hm.create_hotel( "Abba", stars= 3)

print(tesst)