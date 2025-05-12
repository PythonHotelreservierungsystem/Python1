##Facility
class Facility:
    ##attributes
    def __init__(self,facility_id:int, facility_name:str):
        self.facility_id = facility_id
        self.facility_name = facility_name

    ##facility_id Getter & Setter
    @property
    def facility_id(self):
        return self.__facility_id
    @facility_id.setter
    def facility_id(self, value):
        if self.__facility_id : value
        else:
            raise ValueError("Ungültige ID")
        if not facility_id:
            raise ValueError("facility_id ist erforderlich")
        if not isinstance(facility_id, int):
            raise ValueError("facility_id muss eine Zahl sein")

    ##facility_name Getter & Setter
    @property
    def facility_name(self):
        return self.__facility_name
    @facility_name.setter
    def facility_name(self, value):
        self.__facility_name = value
        if value:
            self.__facility_name
        else:
            raise ValueError("Ungültiger Einrichtungsname")
        