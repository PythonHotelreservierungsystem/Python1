from model.invoice import Invoice
from datetime import date, timedelta

print("=== Test: Gültige Rechnung ===")
try:
    future_date = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    invoice1 = Invoice(1, future_date, 250, "B001")
    print("Rechnung erfolgreich erstellt:", invoice1.invoice_id, invoice1.issue_date, invoice1.total_amount, invoice1.booking)
except (ValueError, TypeError) as e:
    print("Fehler bei gültiger Rechnung:", e)

print("\n=== Test: Fehlende invoice_id ===")
try:
    invoice = Invoice(None, future_date, 250, "B002")
    print("Fehler: Fehlende invoice_id wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: invoice_id ist kein int ===")
try:
    invoice = Invoice("eins", future_date, 250, "B003")
    print("Fehler: invoice_id als String wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: issue_date in der Vergangenheit ===")
try:
    past_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    invoice = Invoice(2, past_date, 250, "B004")
    print("Fehler: Vergangenes issue_date wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: issue_date falsches Format ===")
try:
    invoice = Invoice(3, "01-01-2025", 250, "B005")
    print("Fehler: Falsches Datumformat wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test : issue_date als datetime.date direkt übergeben ===")
try:
    invoice = Invoice(4, date.today() + timedelta(days=2), 300, "B006")
    print("Rechnung mit datetime.date erstellt:", invoice.issue_date)
except Exception as e:
    print("Fehler:", e)

print("\n=== Test: Betrag ändern ===")
try:
    invoice1.total_amount = 350
    print("Betrag erfolgreich geändert:", invoice1.total_amount)
except Exception as e:
    print("Fehler beim Ändern des Betrags:", e)

print("\n=== Test: Booking-Zuordnung ändern ===")
try:
    invoice1.booking = "B999"
    print("Booking erfolgreich geändert:", invoice1.booking)
except Exception as e:
    print("Fehler beim Ändern der Booking-ID:", e)