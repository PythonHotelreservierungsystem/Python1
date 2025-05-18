from model.hotel import Hotel

print("=== Test: Gültiges Hotel ===")
try:
    hotel1 = Hotel(1, "Grand Palace", 5, "Bahnhofstrasse 1, Zürich")
    print("Hotel erfolgreich erstellt:", hotel1.hotel_id, hotel1.name, hotel1.stars, hotel1.address)
except ValueError as e:
    print("Fehler bei gültigem Hotel:", e)

print("\n=== Test: hotel_id fehlt ===")
try:
    hotel = Hotel(None, "Grand Palace", 5, "Bahnhofstrasse 1, Zürich")
    print("Fehler: hotel_id None wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: hotel_id ist kein int ===")
try:
    hotel = Hotel("eins", "Grand Palace", 5, "Bahnhofstrasse 1, Zürich")
    print("Fehler: hotel_id als String wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültiger Hotelname (leer) ===")
try:
    hotel1.name = ""
    print("Fehler: Leerer Hotelname wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige Sterne (0) ===")
try:
    hotel1.stars = 0
    print("Fehler: Sterne 0 wurden akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige Sterne (6) ===")
try:
    hotel1.stars = 6
    print("Fehler: Sterne 6 wurden akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Gültige Sterne setzen ===")
try:
    hotel1.stars = 4
    print("Sterne erfolgreich gesetzt:", hotel1.stars)
except ValueError as e:
    print("Fehler bei gültigen Sternen:", e)

print("\n=== Test: Adresse ändern ===")
try:
    hotel1.address = "Seestrasse 10, Luzern"
    print("Adresse erfolgreich geändert:", hotel1.address)
except ValueError as e:
    print("Fehler bei gültiger Adresse:", e)