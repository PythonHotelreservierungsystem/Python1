##RoomType
class RoomType:
    ##attributes
    def __init__(self,room_type_id:int, description:str, max_guests:int):
        self.room_type_id = room_type_id
        self.description = description
        self.max_guests = max_guests
    
    #room_type_id Getter und Setter
    @property
    def room_type_id(self):
        return self.__room_type_id
    @room_type_id.setter
    def room_type_id(self, value):
        self.__room_type_id = value
        if not room_type_id:
            raise ValueError("room_type_id ist erforderlich")
        if not isinstance(room_type_id, int):
            raise ValueError("room_type_id muss eine Zahl sein")
    
    #description Getter und Setter
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        self.__description = value
        if not description:
            raise ValueError("description ist erforderlich")
        if not isinstance(room_type, str):
            raise ValueError("description")

    
    #max_guests Getter und Setter
    @property
    def max_guests(self):
        return self.__max_guests
    @max_guests.setter
    def max_guests(self, value):
        self.__max_guests = value
        if isinstance(value, int) and 1 <= value <= 14:
            self.__max_guests = value
        else:
            raise ValueError("Die maximale Personenanzahl pro Zimmr muss zwischen 1 und 14 liegen.")