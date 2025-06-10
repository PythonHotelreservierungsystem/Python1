import model
from datetime import date
from model.room_type import RoomType
from data_access.address_data_access import AddressDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.admin_data_access import AdminDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.room_type_data_access import RoomTypeDataAccess
from data_access.booking_data_access import BookingDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.base_data_access import BaseDataAccess


class AdminManager:
    def __init__(self,
                 admin_data_access: AdminDataAccess,hotel_da=None,address_da=None,room_da=None,room_type_da=None,
                 booking_da=None,guest_da=None,invoice_da=None):
        self.__admin_da = admin_data_access
        self.__hotel_da = hotel_da
        self.__address_da = address_da
        self.__room_da = room_da
        self.__room_type_da = room_type_da
        self.__booking_da = booking_da
        self.__guest_da = guest_da
        self.__invoice_da = invoice_da
        self.admin_data_access = admin_data_access
        self.logged_in_admin = None

    def update_booking_admin(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool,
                        total_amount: int, guest_id: model.Guest) -> bool:
        return self.__booking_da.update_booking_by_id(booking_id=booking_id, check_in_date=check_in_date, check_out_date=check_out_date,  is_cancelled=is_cancelled, total_amount=total_amount, guest=guest_id)

    def update_address_admin(self, address_id:int, street:str, zip_code:int, city:str) -> bool:
        return self.__address_da.update_address(address_id=address_id, street=street, zip_code=zip_code, city=city)

    def update_hotel_admin(self, hotel_id:int, name:str, stars:int, address_id:int) -> bool:
        return self.__hotel_da.update_hotel(hotel_id=hotel_id, name=name, stars=stars, address_id=address_id)

    def update_guest_admin(self, guest_id:int, firstname: str, lastname: str, email: str, phone_number: str = None) -> model.Guest:
        return self.__guest_da.update_guest(guest_id=guest_id, firstname=firstname, lastname=lastname, email=email, phone_number=phone_number)

    def update_invoice_admin(self, invoice_id: int, issue_date: date, total_amount: int,) -> model.Invoice:
        return self.__invoice_da.update_invoice(invoice_id=invoice_id, issue_date=issue_date, total_amount=total_amount)

    def update_room_admin(self, room_id: int, room_number:int, price_per_night: int) -> bool:
        return self.__room_da.update_room(room_id=room_id, room_number=room_number, price_per_night=price_per_night)

    def update_room_type_admin(self, room_type_id: int, description: str, max_guests: int) -> RoomType:
        return self.__room_type_da.update_room_type(room_type_id=room_type_id, description=description, max_guests=max_guests)


    #für login
    def authenticate(self, username: str, password: str) -> bool:
        admin = self.admin_data_access.login_admin(username, password)
        if admin:
            self.logged_in_admin = admin
            return True
        return False
    def get_logged_in_admin(self):
        return self.logged_in_admin
