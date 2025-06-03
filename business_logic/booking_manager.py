import model

from data_access import RoomDataAccess
from data_access import BookingDataAccess

class BookingManager:
    def __init__(self, booking_da):
        self.__booking_da = booking_da

    def show_bookings(self) -> list[model.Booking]:
        return self.__booking_da.show_bookings_with_hotels()

    ##def bookings_with_hotel(self):
      ##  booking_da = BookingDataAccess()
      ##  bookings = booking_da.show_bookings_with_hotels()

       ## for booking in bookings:
       ##     print(f"Booking: {booking.booking_id}, Room: {booking.room_id}, Hotel: {booking.hotel_id}, Check-in: {booking.check_in}, Check-out: {booking.check_out} ")






xp = BookingManager(BookingDataAccess("../database/hotel_reservation_sample.db"))
tist = xp.show_bookings()
if tist:
    for booking in tist:
        print(f"Booking: {tist.booking_id}, Room: {tist.room_id}, Hotel: {tist.hotel_id}, Check-in: {tist.check_in_date}, Check-out: {tist.check_out_date} ")
else:
    print("Booking not found")