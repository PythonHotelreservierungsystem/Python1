from model.room_type import RoomType

print("=== Test: Gültiger RoomType ===")
try:
    rt1 = RoomType(1, "Einzelzimmer mit Bad", 1)
    print("RoomType erfolgreich erstellt:", rt1.room_type_id, rt1.description, rt1.max_guests)
except ValueError as e:
    print("Fehler bei gültigem RoomType:", e)

print("\n=== Test: room_type_id fehlt ===")
try:
    rt = RoomType(None, "Doppelzimmer", 2)
    print("Fehler: room_type_id None wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: room_type_id ist kein int ===")
try:
    rt = RoomType("eins", "Doppelzimmer", 2)
    print("Fehler: room_type_id als String wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Leere Beschreibung ===")
try:
    rt1.description = ""
    print("Fehler: Leere Beschreibung wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Beschreibung ist kein String ===")
try:
    rt1.description = 123
    print("Fehler: Beschreibung als Zahl wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test : Ungültige max_guests (zu hoch) ===")
try:
    rt1.max_guests = 20
    print("Fehler: max_guests > 14 wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige max_guests (zu niedrig) ===")
try:
    rt1.max_guests = 0
    print("Fehler: max_guests < 1 wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Gültige Änderung max_guests ===")
try:
    rt1.max_guests = 4
    print("max_guests erfolgreich geändert:", rt1.max_guests)
except ValueError as e:
    print("Fehler bei gültiger Änderung:", e)
