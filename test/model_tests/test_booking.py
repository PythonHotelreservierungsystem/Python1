from model.booking import Booking
from datetime import date, timedelta

print("=== Test: Gültige Buchung ===")
try:
    checkin = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    checkout = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")
    booking1 = Booking("B001", checkin, checkout, False, 450.00, 1)
    print("Buchung erfolgreich erstellt:", booking1)
except ValueError as e:
    print("Fehler bei gültiger Buchung:", e)

print("\n=== Test: Buchung ohne booking_id. ===")
try:
    booking = Booking(None, checkin, checkout, False, 450.00, 1)
    print("Fehler: Buchung ohne booking_id wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: booking_id ist kein String ===")
try:
    booking = Booking(123, checkin, checkout, False, 450.00, 1)
    print("Fehler : booking_id als int wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Check-In liegt in der Vergangenheit ===")
try:
    past_checkin = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    booking = Booking("B002", past_checkin, checkout, False, 450.00, 1)
    print("Fehler: Vergangener Check-In wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Check-Out liegt in der Vergangenheit ===")
try:
    past_checkout = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    booking = Booking("B003", checkin, past_checkout, False, 450.00, 1)
    print("Fehler: Vergangener Check-Out wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Check-Out vor Check-In ===")
try:
    checkin = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")
    checkout = (date.today() + timedelta(days=2)).strftime("%Y-%m-%d")
    booking = Booking("B004", checkin, checkout, False, 450.00, 1)
    print("Fehler: Check-Out vor Check-In wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)