from datetime import datetime, date

class Booking:
    def __init__(self, booking_id: int, hotel_id: int, room_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float, guest: int):
        if not booking_id:
            raise ValueError("booking_id ist erforderlich")
        if not isinstance(booking_id, str):
            raise ValueError("booking_id muss ein String sein")
        self.__booking_id = booking_id
        self.hotel_id = hotel_id ##allwe überflüssig jetzt
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.total_amount = total_amount
        self.guest = guest

    @property
    def check_in_date(self):
        return self.__checkin_date

    @check_in_date.setter
    def check_in_date(self, value):
        parsed_date = datetime.strptime(value, "%Y-%m-%d").date()
        if parsed_date < date.today():
            raise ValueError("CheckIn Date darf nicht in der Vergangenheit liegen")
        self.__check_in_date = parsed_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        parsed_date = datetime.strptime(value, "%Y-%m-%d").date()
        if parsed_date < date.today():
            raise ValueError("CheckOut Date darf nicht in der Vergangenheit liegen")
        if hasattr(self, '_Booking__checkin_date') and parsed_date < self.checkin_date:
            raise ValueError("CheckOut Date darf nicht vor dem CheckIn Date liegen")
        self.__check_out_date = parsed_date

    def __str__(self):
        return f"Booking({self.__booking_id}, {self.checkin_date}, {self.checkout_date}, {self.is_cancelled}, {self.total_amount}, {self.guest})"
