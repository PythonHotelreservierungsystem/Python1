##Facility
class Facility:
    ##attributes
    def __init__(self, facility_id: int, facility_name: str):
        if facility_id is None:
            raise ValueError("facility_id ist erforderlich")

        if not isinstance(facility_id, int):
            raise ValueError("facility_id muss eine Zahl sein")

        self.__facility_id = facility_id
        self.facility_name = facility_name

    ##facility_id Getter & Setter
    @property
    def facility_id(self):
        return self.__facility_id

    ##facility_name Getter & Setter
    @property
    def facility_name(self):
        return self.__facility_name
    @facility_name.setter
    def facility_name(self, value):
        if not value:
            raise ValueError("Ungültiger Einrichtungsname")
        self.__facility_name = value
        