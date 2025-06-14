from datetime import datetime, date

from model import Booking

##Invoice
class Invoice:
    #attributes
    def __init__(self, invoice_id: int, issue_date: date, total_amount: int, booking: Booking):
        self.__invoice_id = invoice_id
        self.issue_date = issue_date
        self.total_amount = total_amount
        self.booking = booking
        if not invoice_id:
            raise ValueError("invoice_id ist erforderlich")
        if not isinstance(invoice_id, int):
            raise ValueError("invoice_id muss eine Zahl sein")
    
    ##invoice_id Getter & Setter
    @property
    def invoice_id(self):
        return self.__invoice_id

    ##issue_date Getter & Setter
    @property
    def issue_date(self):
        return self.__issue_date
    @issue_date.setter
    def issue_date(self, value):
        if isinstance(value, str):
            try:
                parsed_date = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("issue_date muss im Format YYYY-MM-DD sein")
        elif isinstance(value, date):
            parsed_date = value
        else:
            raise TypeError("issue_date muss ein String (YYYY-MM-DD) oder ein datetime.date sein")
        # Validierung: kein Datum in der Vergangenheit
        if parsed_date < date.today():
            raise ValueError("Issue Date darf nicht in der Vergangenheit liegen")

        self.__issue_date = parsed_date

    ##total_amount Getter & Setter
    @property
    def total_amount(self):
        return self.__total_amount
    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value


    ##booking Getter & Setter
    @property
    def booking(self):
        return self.__booking
    @booking.setter
    def booking(self, value):
        self.__booking = value