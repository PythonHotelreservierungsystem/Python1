##Address
class Address:
    #attributes
    def __init__(self, address_id:int, street:str, city:str, zip_code:int):
        if not address_id:
            raise ValueError("address_id ist erforderlich")
        if not isinstance(address_id, int):
            raise ValueError("address_id muss eine Zahl sein")

        self.__address_id = address_id
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.address_id}, street={self.street}, city={self.city}, zip_code={self.zip_code})"

    #address_id Getter & Setter
    @property
    def address_id(self):
        return self.__address_id
    
    #street Getter & Setter
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, value):
        if value and " " in value:
            self.__street = value
        else:
            raise ValueError("Strasse muss Haus-Nr. enthalten")
    
    #city Getter & Setter
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,value):
        if value:
            self.__city = value
        else:
            raise ValueError("Ungültiger Ort") 
    
    #zip Getter & Setter
    @property
    def zip_code(self):
        return self.__zip_code
    @zip_code.setter
    def zip_code(self, value):
        if value:
            self.__zip_code = value
        else:
            raise ValueError("Ungültige PLZ")