##Invoice
class Invoice:
    #attributes
    def __init__(self,invoice_id:str, issue_date:str, total_amount:int, booking:str):
        self.invoice_id = invoice_id
        self.issue_date = issue_date
        self.total_amount = total_amount
        self.booking = booking
    
    ##invoice_id Getter & Setter
    @property
    def invoice_id(self):
        return self.__invoice_id
    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
        if not invoice_id:
            raise ValueError("invoice_id ist erforderlich")
        if not isinstance(invoice_id, int):
            raise ValueError("invoice_id muss eine Zahl sein")


    ##issue_date Getter & Setter
    @property
    def issue_date(self):
        return self.__issue_date
    @issue_date.setter
    def issue_date(self, value):
        self.__issue_date = value
        if value < date.today(): 
            raise ValueError("Issue Date darf nicht in der vergangenheit liegen")


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