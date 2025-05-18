from model.guest import Guest

print("=== Test: Gültiger Gast ===")
try:
    guest1 = Guest(1, "Max", "Muster", "max@test.com")
    print("Guest erfolgreich erstellt:", guest1.guest_id, guest1.firstname, guest1.lastname, guest1.email)
except ValueError as e:
    print("Fehler bei gültigem Gast:", e)

print("\n=== Test: Leerer Vorname setzen ===")
try:
    guest1.firstname = ""
    print("Fehler: Leerer Vorname wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Leerer Nachname setzen ===")
try:
    guest1.lastname = ""
    print("Fehler: Leerer Nachname wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige E-Mail setzen ===")
try:
    guest1.email = "ungültigeemail"
    print("Fehler: Ungültige E-Mail wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige Adresse setzen ===")
try:
    guest1.address = None
    print("Fehler: Ungültige Adresse wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Gültige Adresse setzen ===")
try:
    guest1.address = ["Musterstrasse 1", "8000 Zürich"]
    print("Adresse erfolgreich gesetzt:", guest1.address)
except ValueError as e:
    print("Fehler bei gültiger Adresse:", e)

print("\n=== Test: Booking hinzufügen ===")
try:
    booking_dummy = "DummyBookingObject"
    guest1.add_booking(booking_dummy)
    print("Booking hinzugefügt:", guest1.bookings)
except Exception as e:
    print("Fehler beim Hinzufügen einer Buchung:", e)