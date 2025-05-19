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


    def show_hotel_by_city(self, city: str) -> model.Hotel:
        return self.__hotel_da.show_hotel_by_id(1)

xp = HotelManager(HotelDataAccess("../../database/hotel_reservation_sample.db"))
tist = xp.show_hotel_by_city("Basel")

if tist:
    print(f"Hotel {tist.name} {tist.stars} {tist.address}")
else:
    print("Hotel not found")


hm = HotelManager(HotelDataAccess("../../database/hotel_reservation_sample.db"))
tesst = hm.show_hotels(hotel_id=1)


if tesst:
    print(f"Hotel '{tesst.name}' (ID: {tesst.hotel_id}) - {tesst.stars} stars, Address ID {tesst.address}")
##else:
   ## print("Hotel not found")