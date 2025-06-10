from __future__ import annotations
import model
from model import Address
from model import Hotel
from model import Booking
from model import Guest
from data_access.base_data_access import BaseDataAccess


class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(self,
                         firstname: str,
                         lastname: str,
                         email:str,
                         address_id: model.Address,
                         booking_id: model.Booking) -> model.Guest:
        if firstname is None or lastname is None or email is None:
            raise ValueError("firstname and lastname and email are required")

        sql = """
        INSERT INTO Guest(first_name, last_name, email)
        VALUES (?, ?, ?)"""
        params = tuple([
            firstname,
            lastname,
            email,
            address_id,
            booking_id
        ])
        last_row_id, row_count = self.execute(sql, params)

        return model.Guest(
            guest_id=row_count,
            firstname=firstname,
            lastname=lastname,
            email=email

        )
    #Userstory 10
    def update_guest(self, guest_id: int, firstname: str, lastname: str, email: str, phone_number: str=None) -> model.Guest:
        sql = """
        UPDATE Guest SET first_name= ?, last_name= ?, email = ?, phone_number = ? WHERE guest_id = ?
        """
        params = (firstname, lastname, email, phone_number, guest_id)
        _, row_count = self.execute(sql, params)
        return row_count > 0

    def show_all_guests(self):
        sql = "SELECT guest_id, first_name, last_name, email, phone_number FROM Guest"
        guests_raw = self.fetchall(sql)

        for row in guests_raw:
            print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Email: {row[3]}, Telefon: {row[4]}")

    def read_all_guests(self) -> list[Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, email, phone_number
        FROM Guest"""
        guests = self.fetchall(sql)
        return_list = []
        for guest_id, firstname, lastname, email, phone_number in guests:
            return_list.append(Guest(guest_id, firstname, lastname, email, phone_number))
        return return_list
