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

#
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

    #User Story 6
    def update_booking(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: int, guest_id: model.Guest)-> bool:
        return self.__booking_da.update_booking_by_id(booking_id=booking_id,
                                                      check_in_date=check_in_date,
                                                      check_out_date=check_out_date,
                                                      is_cancelled=is_cancelled,
                                                      total_amount=total_amount,
                                                      guest=guest_id)

    ##Hilfsfunktion für Bookings
    def delete_booking(self, booking_id: int)-> bool:
        return self.__booking_da.delete_booking_by_id(booking_id)

    #User Story 5
    def create_invoice_with_booking(self, guest: model.Guest, room: model.Room, check_in_date: date,
                                    check_out_date: date, invoice_da: InvoiceDataAccess) -> model.Invoice:

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
        if not neue_buchung:
            print("Buchung konnte nicht erstellt werden.")
            return None

        issue_date = check_out_date
        invoice = invoice_da.create_invoice(issue_date=issue_date, total_amount=gesamtpreis, booking_id=neue_buchung.booking_id)
        return invoice