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
        INSERT INTO Guest(firstname, lastname, email)
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
