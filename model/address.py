class Address:
    def __init__(self, address_id: int, street: str, city: str, zip_code: int):
        self.__address_id = address_id
        self.street = street
        self.city = city
        self.zip_code = zip_code

        if not isinstance(address_id, int):
            raise ValueError("address_id muss eine Zahl sein")

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(id={self.address_id}, street={self.street}, "
                f"city={self.city}, zip_code={self.zip_code})")

    @property
    def address_id(self):
        return self.__address_id

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        if value and " " in value:
            self.__street = value
        else:
            raise ValueError("Strasse muss Haus-Nr. enthalten")

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if value and isinstance(value, str):
            self.__city = value
        else:
            raise ValueError("Ungültiger Ort")

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value):
        if isinstance(value, int):
            self.__zip_code = value
        else:
            raise ValueError("Ungültige PLZ")
