##Booking
class Booking:
    #attributes
    def __init__(self,booking_id:str, checkin_date:str, checkout_date:str, is_cancelled:bool, total_amount:float, 
                 guest:int):
        self.booking_id = booking_id
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.is_cancelled = is_cancelled
        self.total_amount = total_amount
        self.guest = guest        
        
    ##booking_id Getter & Setter
    @property
    def booking_id(self):
        return self.__booking_id
    @booking_id.setter
    def booking_id(self, value):
        self.__booking_id = value
        if not booking_id:
            raise ValueError("booking_id ist erforderlich")
        if not isinstance(booking_id, int):
            raise ValueError("booking_id muss eine Zahl sein")


    ##checkin_date Getter & Setter
    @property
    def checkin_date(self):
        return self.__checkin_date
    @checkin_date.setter
    def checkin_date(self, value):
        self.__checkin_date = value
        if value < date.today(): 
            raise ValueError("CheckIn Date darf nicht in der vergangenheit liegen")


    ##checkout_date Getter & Setter
    @property
    def checkout_date(self):
        return self.__checkout_date
    @checkout_date.setter
    def checkout_date(self, value):
        self.__checkout_date = value
        self.__checkout_date = value
        if value < date.today(): 
            raise ValueError("CheckOut Date darf nicht in der vergangenheit liegen")
        if value < checkin_date():
            raise ValueError("CheckOut Date darf nicht vor dem CheckIn Date liegen")

    ##is_cancelled Getter & Setter
    @property
    def is_cancelled(self):
        return self.__is_cancelled
    @is_cancelled.setter
    def is_cancelled(self, value):
        self.__is_cancelled = value
        if not value != bool:
            RaiseTypeError("is_cancelled muss Ja oder Nein sein")


    ##total_amount Getter & Setter
    @property
    def total_amount(self):
        return self.__total_amount
    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
        if value:
            self.__total_amount = value
        else:
            raise ValueError("Ungültiger Betrag")


    ##guest Getter & Setter
    @property
    def guest(self):
        return self.__guest
    @guest.setter
    def guest(self, value):
        self.__guest = valued