import sqlite3

def add_phone_number_to_guest():
    conn = sqlite3.connect("../database/hotel_reservation_sample.db")
    conn.execute("ALTER TABLE Guest ADD COLUMN phone_number TEXT")
    conn.commit()
    conn.close()
    print("Spalte 'phone_number' wurde hinzugefügt.")

# if __name__ == "__main__":
#     add_phone_number_to_guest()