##Room
class Room:
    #attributes #?facilites als externe Facility Liste führen? #?room_type als string oder integer?
    def __init__(self, room_id:int, room_no:int, price_per_night:float, room_type:RoomType, hotel:str, facilities:list):
        self.room_id = room_id
        self.room_no = room_no
        self.price_per_night = price_per_night
        self.room_type = room_type 
        self.hotel = hotel
        self.facilities = facilities

    #room_id Getter und Setter
    @property
    def room_id(self):
        return self.__room_id
    @room_id.setter
    def room_id(self, value):
        self.__room_id = value
        if not room_id:
            raise ValueError("room_id ist erforderlich")
        if not isinstance(room_id, int):
            raise ValueError("room_id muss eine Zahl sein")
    
    #room_no Getter und Setter
    @property
    def room_no(self):
        return self.__room_no
    @room_no.setter
    def room_no(self, value):
        self.__room_no = value
        if not room_no:
            raise ValueError("room_no ist erforderlich")
        if not isinstance(room_no, int):
            raise ValueError("room_no muss eine Zahl sein")

    #price_per_night Getter und Setter
    @property
    def price_per_night(self) -> float:
        return self.__price_per_night
    @price_per_night.setter
    def price_per_night(self, value: float):
        if type(value) != float:
            raise TypeError("Unügltiger typ für Preis")
        self.__price_per_night = value

    #room_type Getter und Setter
    @property
    def room_type(self):
        return self.__room_type
    @room_type.setter
    def room_type(self, value):
        self.__room_type = value
        
    #hotel Getter und Setter
    @property
    def hotel(self):
        return self.__hotel
    @hotel.setter
    def hotel(self, value):
        self.__hotel = value

    #facilities Getter und Setter
    @property
    def facilities(self):
        return self.__facilities
    @facilities.setter
    def facilities(self, value):
        self.__facilities = value
        