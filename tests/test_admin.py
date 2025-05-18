from model.admin import Admin

print("=== Test: Gültiger Admin ===")
try:
    admin1 = Admin(1, "adminuser", "Abc123$%", "admin@test.com")
    print("Admin erfolgreich erstellt:", admin1.username, admin1.email)
except ValueError as e:
    print("Fehler bei gültigem Admin:", e)

print("\n=== Test: admin_id fehlt ===")
try:
    admin2 = Admin(None, "adminuser", "Abc123$%", "admin@test.com")
    print("Fehler: admin_id None wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: admin_id kein int ===")
try:
    admin2 = Admin("eins", "adminuser", "Abc123$%", "admin@test.com")
    print("Fehler: admin_id als String wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültiger Username (leer) ===")
try:
    admin1.username = ""
    print("Fehler: Leerer Username wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültige Email ===")
try:
    admin1.email = "admin[at]mail"
    print("Fehler: Ungültige Email wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültiges Passwort – zu kurz ===")
try:
    admin1.password = "a1$"
    print("Fehler: Zu kurzes Passwort wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültiges Passwort – keine Zahl ===")
try:
    admin1.password = "Abcdefg$"
    print("Fehler: Passwort ohne Zahl wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Ungültiges Passwort – kein Sonderzeichen ===")
try:
    admin1.password = "Abc12345"
    print("Fehler: Passwort ohne Sonderzeichen wurde akzeptiert!")
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== Test: Gültiges Passwort setzen ===")
try:
    admin1.password = "NeuPass1!"
    print("Passwort erfolgreich gesetzt.")
except ValueError as e:
    print("Fehler bei gültigem Passwort:", e)