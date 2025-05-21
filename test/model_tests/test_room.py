from model.room import Room

print("=== Test: Gültiges Zimmer ===")
try:
    room1 = Room(1, 101, 120.0, "Einzelzimmer", "Hotel Zürich", ["TV", "WLAN"])
    print("Zimmer erfolgreich erstellt:", room1.room_id, room1.room_no, room1.price_per_night, room1.room_type, room1.hotel, room1.facilities)
except Exception as e:
    print("Fehler bei gültigem Zimmer:", e)

print("\n=== Test: Kein room_id ===.")
try:
    room = Room(None, 101, 120.0, "Einzelzimmer", "Hotel Zürich", ["TV"])
    print("Fehler: room_id None wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test : room_id ist kein int ===")
try:
    room = Room("eins", 101, 120.0, "Einzelzimmer", "Hotel Zürich", ["TV"])
    print("Fehler: room_id als String wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige room_no ===")
try:
    room1.room_no = "A1"
    print("Fehler: Ungültige room_no wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültiger Preis (int statt float) ===")
try:
    room1.price_per_night = 100  # int statt float
    print("Fehler: Preis als int wurde akzeptiert!")
except TypeError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Gültige Preisänderung ===")
try:
    room1.price_per_night = 150.0
    print("Preis erfolgreich geändert:", room1.price_per_night)
except Exception as e:
    print("Fehler bei gültigem Preis:", e)

print("\n=== Test: Zimmerausstattung ändern ===")
try:
    room1.facilities = ["TV", "WLAN", "Balkon"]
    print("Ausstattung erfolgreich geändert:", room1.facilities)
except Exception as e:
    print("Fehler beim Setzen der Ausstattung:", e)

print("\n=== Test: Hotelzuweisung ändern ===")
try:
    room1.hotel = "Hotel Bern"
    print("Hotel erfolgreich geändert:", room1.hotel)
except Exception as e:
    print("Fehler beim Setzen des Hotels:", e)

print("\n=== Test: Room-Type setzen ===")
try:
    room1.room_type = "Suite"
    print("Room-Type erfolgreich gesetzt:", room1.room_type)
except Exception as e:
    print("Fehler beim Setzen des Room-Types:", e)