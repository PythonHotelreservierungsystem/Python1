import data_access
import model
from typing import List

class HotelManager:
    def __init__(self):
        self.__hotels_da = data_access.hotel_data_access()

    def read_hotels_by_cty(self,city: str) -> List[model.Hotel]:
        return self.__hotels_da.read_hotels_by_city(city)