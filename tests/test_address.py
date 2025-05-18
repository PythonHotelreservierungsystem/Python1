from model.address import Address

print("=== Test: Gültige Adresse ===")
try:
    address1 = Address(1, "Musterstrasse 10", "Zürich", 8000)
    print("Adresse erfolgreich erstellt:", address1)
except ValueError as e:
    print("Fehler bei gültiger Adresse:", e)

print("\n=== Test: Ungültige address_id (kein int) ===")
try:
    address2 = Address("eins", "Musterstrasse 10", "Zürich", 8000)
    print("Fehler: Ungültige address_id wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige Strasse (ohne Hausnummer) ===")
try:
    address1.street = "Musterstrasse"  # kein Leerzeichen = keine Hausnummer
    print("Fehler: Strasse ohne Hausnummer wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige Stadt (None) ===")
try:
    address1.city = None
    print("Fehler: Ungültiger Ort wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige PLZ (String statt int) ===")
try:
    address1.zip_code = "8000"
    print("Fehler: Ungültige PLZ wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Gültige Änderungen ===")
try:
    address1.street = "Bahnhofstrasse 5"
    address1.city = "Bern"
    address1.zip_code = 3000
    print("Adresse erfolgreich geändert:", address1)
except ValueError as e:
    print("Fehler bei gültiger Änderung:", e)