import model
from datetime import date
from data_access.booking_data_access import BookingDataAccess
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.room_data_access import RoomDataAccess
from business_logic.room_manager import RoomManager

class BookingManager:
    def __init__(self, booking_da: BookingDataAccess, room_manager: RoomManager):
        self.__booking_da = booking_da
        self.__room_manager = room_manager

    def show_bookings(self) -> list[model.Booking]:
        return self.__booking_da.show_bookings_with_hotels()


    ## Create Booking User story 4
    def create_new_booking(self, guest: model.Guest, check_in_date: date, check_out_date: date):
        verfuegbare_zimmer = self.__room_manager.find_available_rooms_by_dates(check_in_date, check_out_date)
        if not verfuegbare_zimmer:
            print("Es gibt keine verfügbaren Räume für Ihren gewünschten Zeitraum.")
            return None

        print("Verfügbare Zimmer:")
        for zimmer in verfuegbare_zimmer:
            print(f"Room-ID: {zimmer.room_id} | Typ: {zimmer.type_id} | Preis/Nacht: {zimmer.price_per_night}")

        while True:
            try:
                gewuenschte_id = int(input("Geben Sie die Room-ID des gewünschten Raumes an: "))
                if gewuenschte_id == 1:
                    raise ValueError("Zimmer ist schon besetzt")
                gewuenschtes_zimmer = next((z for z in verfuegbare_zimmer if z.room_id == gewuenschte_id), None)
                if gewuenschtes_zimmer:
                    break
                else:
                    print("Kein Zimmer mit dieser ID verfügbar. Bitte erneut versuchen.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine gültige Ganzzahl eingeben.")

        total_naechte = (check_out_date - check_in_date).days
        gesamtpreis = total_naechte * gewuenschtes_zimmer.price_per_night

        neue_buchung = self.__booking_da.create_booking(
            guest_id=guest,
            room_id=gewuenschtes_zimmer,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            is_cancelled=False,
            total_amount=gesamtpreis
        )
        print("Buchung erfolgreich erstellt.")
        return neue_buchung

    ##Hilfsfunktion für Bookings
    def delete_booking(self, booking_id: int)-> bool:
        return self.__booking_da.delete_booking_by_id(booking_id)

