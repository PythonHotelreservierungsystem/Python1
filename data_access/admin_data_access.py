import sqlite3
from model.admin import Admin


class AdminDataAccess:
    def __init__(self, db_path="database/hotel_reservation_sample.db"):
        self.db_path = db_path
    #Für Admin User Story
    def create_admin(self, admin: Admin):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO admin (username, password, email, vorname, nachname)
            VALUES (?, ?, ?, ?, ?)
        """, (admin.username, admin.password, admin.email, admin.vorname, admin.nachname))
        conn.commit()
        conn.close()

    #Für Admin User Story
    def get_all_admins(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT admin_id, username, password, email, vorname, nachname FROM admin")
        rows = cursor.fetchall()
        conn.close()
        return [Admin(*row) for row in rows]

    # Für Admin User Story
    def login_admin(self, username: str, password: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT admin_id, username, password, email, vorname, nachname
                       FROM admin
                       WHERE username = ?
                         AND password = ?
                       """, (username, password))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Admin(*row)
        return None