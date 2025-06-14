
from model import Address
##Hotel
class Hotel:
    #attributes
    def __init__(self, hotel_id:int, name:str, stars:int, address:Address):
        if not hotel_id:
            raise ValueError("hotel_id ist erforderlich")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id muss eine Zahl sein")
        self.__hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.address = address
        self.__rooms = []

    ##hotel_id Getter
    @property
    def hotel_id(self):
        return self.__hotel_id

    ##name Getter & Setter
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
        if value:
            self.__name = value
        else:
            raise ValueError("Ungültiger Hotelname")

    ##stars Getter & Setter
    @property
    def stars(self):
        return self.__stars
    @stars.setter
    def stars(self, value):
        self.__stars = value
        if isinstance(value, int) and 1 <= value <= 5:
            self.__stars = value
        else:
            raise ValueError("Steren müssen eine ganze Zahl zwischen 1 und 5 sein.")

    ##address Getter & Setter
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value):
        self.__address = value

    ##rooms Getter & Setter
    @property
    def rooms(self):
        return self.__rooms
    @rooms.setter
    def rooms(self, value):
        self.__rooms = value