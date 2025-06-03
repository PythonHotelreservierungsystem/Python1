import model
import data_access

from data_access import RoomDataAccess
from data_access import BookingDataAccess

class BookingManager:
    def __init__(self, booking_id):
        self.__booking_da = data_access.BookingDataAccess()

    def list_bookings_by_room(self):
        booking_da = BookingDataAccess()
        bookings = booking_da.show_bookings_with_hotels()

        for booking in bookings:
            print(f"Booking: {booking.booking_id}, Room: {booking.room_id}, Hotel: {booking.hotel_id}, Check-in: {booking.check_in}, Check-out: {booking.check_out} ")

