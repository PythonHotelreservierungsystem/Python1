from datetime import datetime, date

from model.guest import Guest

class Booking:
    def __init__(self, booking_id: int, hotel_id: int, room_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float, guest: Guest):
        if not booking_id:
            raise ValueError("booking_id ist erforderlich")
        if not isinstance(booking_id, int):
            raise ValueError("booking_id muss ein String sein")
        self.__booking_id = booking_id
        self.hotel_id = hotel_id ##allwe überflüssig jetzt
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.total_amount = total_amount
        self.guest = guest
#
    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        if isinstance(value, date):
            parsed_date = value
        elif isinstance(value, str):
            parsed_date = datetime.strptime(value, "%Y-%m-%d").date()
        else:
            raise TypeError("check_in_date muss ein String (YYYY-MM-DD) oder ein datetime.date sein")
        ##if parsed_date < date.today():
        ##    raise ValueError("CheckIn Date darf nicht in der Vergangenheit liegen")
        self.__check_in_date = parsed_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        if isinstance(value, date):
            parsed_date = value
        elif isinstance(value, str):
            parsed_date = datetime.strptime(value, "%Y-%m-%d").date()
        else:
            raise TypeError("check_out_date muss ein String (YYYY-MM-DD) oder ein datetime.date sein")
        #if parsed_date < date.today():
            #raise ValueError("CheckOut Date darf nicht in der Vergangenheit liegen")
        if hasattr(self, '_Booking__checkin_date') and parsed_date < self.check_in_date:
            raise ValueError("CheckOut Date darf nicht vor dem CheckIn Date liegen")
        self.__check_out_date = parsed_date

    def __str__(self):
        return f"Booking({self.__booking_id}, {self.check_in_date}, {self.check_out_date}, {self.is_cancelled}, {self.total_amount}, {self.guest})"
