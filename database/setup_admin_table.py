import sqlite3

def create_admin_table():
    conn = sqlite3.connect("../database/hotel_reservation_sample.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        vorname TEXT,
        nachname TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("Admin-Tabelle erfolgreich erstellt (falls noch nicht vorhanden).")

# if __name__ == "__main__":
#     create_admin_table()