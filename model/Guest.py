class Guest:
    def __init__(self, guest_id: int, firstname: str, lastname: str, email: str, address: str):
        self.guest_id = guest_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.bookings = []  # Association mit Booking

    ## add_booking Methode
    def add_booking(self, booking):
        self.bookings.append(booking)

    ## guest_id Getter & Setter
    @property
    def guest_id(self):
        return self.__guest_id

    @guest_id.setter
    def guest_id(self, value):
        if value:
            self.__guest_id = value
        else:
            raise ValueError("Ungültige ID")
        if not guest_id:
            raise ValueError("guest_id ist erforderlich")
        if not isinstance(guest_id, int):
            raise ValueError("guest_id muss eine Zahl sein")

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
