import model
from datetime import date
from data_access.booking_data_access import BookingDataAccess
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

if __name__ == "__main__":
    from model import Hotel, Address, Guest, Room, RoomType
    from data_access.booking_data_access import BookingDataAccess
    from data_access.room_data_access import RoomDataAccess
    from data_access.facility_data_access import FacilityDataAccess
    from business_logic.room_manager import RoomManager
    from business_logic.booking_manager import BookingManager
    from datetime import date

    # Dummy-Adresse und Hotel
    adresse = Address(address_id=1, street="Teststrasse 10", city="Olten", zip_code=4600)
    hotel = Hotel(hotel_id=1, name="Hotel Test", stars=3, address=adresse)

    # Dummy RoomType und Room
    room_type = RoomType(room_type_id=1, description="Standardzimmer", max_guests=2)
    zimmer = Room(room_id=1, room_number="101", price_per_night=120.0, room_type=room_type, hotel=hotel)

    # Dummy Guest (IDs müssen existieren in der DB)
    gast = Guest(guest_id=1, firstname="Max", lastname="Muster", email="max@muster.ch")

    # Manager & DAO Setup
    db_path = "../database/hotel_reservation_sample.db"
    booking_dao = BookingDataAccess(db_path)
    room_dao = RoomDataAccess(db_path)
    facility_dao = FacilityDataAccess(db_path)
    room_manager = RoomManager(room_data_access=room_dao, facility_data_access=facility_dao)
    booking_manager = BookingManager(booking_da=booking_dao, room_manager=room_manager)

    # Buchungen vor dem Einfügen
    print("Buchungen vor dem Einfügen:")
    for b in booking_manager.show_bookings():
        print(f"Booking-ID: {b.booking_id}, Room-ID: {b.room_id}, Hotel-ID: {b.hotel_id}, Check-in: {b.check_in_date}, Check-out: {b.check_out_date}")

    # Buchung erstellen
    check_in = date(2025, 8, 10)
    check_out = date(2025, 8, 15)
    neue_buchung = booking_dao.create_booking(
        guest_id=gast,
        room_id=zimmer,
        check_in_date=check_in,
        check_out_date=check_out,
        is_cancelled=False,
        total_amount=zimmer.price_per_night * (check_out - check_in).days
    )

    # Neue Buchung anzeigen
    print("\nNeue Buchung erstellt:")
    print(f"Booking-ID: {neue_buchung.booking_id}, Guest-ID: {neue_buchung.guest}, Room-ID: {neue_buchung.room_id}")

    # Buchungen nach dem Einfügen
    print("\nBuchungen nach dem Einfügen:")
    for b in booking_manager.show_bookings():
        print(f"Booking-ID: {b.booking_id}, Room-ID: {b.room_id}, Hotel-ID: {b.hotel_id}, Check-in: {b.check_in_date}, Check-out: {b.check_out_date}")