from model.facility import Facility

print("=== Test: Gültige Facility ===")
try:
    facility1 = Facility(1, "Fitnessraum")
    print("Facility erfolgreich erstellt:", facility1.facility_id, facility1.facility_name)
except ValueError as e:
    print("Fehler bei gültiger Facility:", e)

print("\n=== Test: Facility ohne ID ===")
try:
    facility = Facility(None, "Sauna")
    print("Fehler: Facility ohne ID wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Facility-ID ist kein int ===")
try:
    facility = Facility("eins", "Pool")
    print("Fehler: Facility-ID als String wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Leerer Facility-Name ===")
try:
    facility1.facility_name = ""
    print("Fehler: Leerer Facility-Name wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Gültiger Facility-Name ändern ===")
try:
    facility1.facility_name = "Spa-Bereich"
    print("Facility-Name erfolgreich geändert:", facility1.facility_name)
except ValueError as e:
    print("Fehler beim Ändern des Namens:", e)