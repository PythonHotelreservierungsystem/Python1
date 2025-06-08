import model

from data_access import RoomDataAccess
from data_access import BookingDataAccess
import business_logic.room_manager as room_manager



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


    # Create Booking User story 4
    def create_new_booking(self, guest: model.Guest, room: model.room, check_in_date: int, check_out_date: int,
                           is_cancelled: bool, total_amount: float) -> model.Booking:
        verfuegbare_zimmer = self.room_manager.find_available_rooms_by_dates(check_in_date, check_out_date)
        if not(verfuegbare_zimmer):
            print("Es gibt keine Verfügbaren Räume für Ihren gewünschten Zeitraum")
            return None

        print(verfuegbare_zimmer)
        for idx, room in enumerate(verfuegbare_zimmer):
            print(f"Room: {room.room_id}")

        gewuenschtes_zimmer = input("Geben Sie die Room_Id des gewünschten Raumes an")

        gewuenschtes_zimmer = verfuegbare_zimmer.get(gewuenschtes_zimmer)
        total_naechte = (check_out_date - check_in_date)
        gesamtpreis = total_naechte * room.price_per_night

        neue_buchung = self.__booking_da.create_new_booking(
            guest=guest,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            is_cancelled = False,
            total_amount = gesamtpreis)

        return neue_buchung



