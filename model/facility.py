##Facility
class Facility:
    ##attributes
    def __init__(self, facility_id: str, facility_name: str):
        if facility_id is None or not str(facility_id).isdigit():
            raise ValueError("facility_id muss eine Zahl sein")
        self.facility_id = int(facility_id)
        self.facility_name = facility_name

    ##facility_id Getter & Setter

    def facility_id(self):
        return self.__facility_id
#
    ##facility_name Getter & Setter
    @property
    def facility_name(self):
        return self.__facility_name
    @facility_name.setter
    def facility_name(self, value):
        if not value:
            raise ValueError("Ungültiger Einrichtungsname")
        self.__facility_name = value
        