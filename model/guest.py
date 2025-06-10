##Guest
class Guest:
    def __init__(self, guest_id: int, firstname: str, lastname: str, email: str, phone_number: str = None):
        if not guest_id:
            raise ValueError("guest_id ist erforderlich")
        if not isinstance(guest_id, int):
            raise ValueError("guest_id muss eine Zahl sein")
        self.__guest_id = guest_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.__address = [] # Association mit address
        self.bookings = []  # Association mit Booking
        self.phone_number = phone_number

    ## add_booking Methode
    def add_booking(self, booking):
        self.bookings.append(booking)

    ## guest_id Getter & Setter
    @property
    def guest_id(self):
        return self.__guest_id

    ## firstname Getter & Setter
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value: str):
        if value:
            self.__firstname = value
        else:
            raise ValueError("Ungültiger Vorname")

    ## lastname Getter & Setter
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        if value:
            self.__lastname = value
        else:
            raise ValueError("Ungültiger Nachname")

    ## email Getter & Setter
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Ungültige Email")
        self.__email = value

    ## address Getter & Setter
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if value:
            self.__address = value
        else:
            raise ValueError("Ungültige Adresse")

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if value is None or (isinstance(value, str) and value.strip() != ""):
            self.__phone_number = value
        else:
            raise ValueError("Ungültige Telefonnummer")