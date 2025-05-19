from __future__ import annotations

import model

from model import Address

from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
##Do müend bi de Models no ergänzt werde mit Country und so u
    def create_address(
            self,
            street: str,
            street_number: int,
            city: str,
            postal_code: int,
            country: str
    ) -> model.Address:
        if street is None:
            raise ValueError("street cannot be None")
        if street_number is None:
            raise ValueError("street number cannot be None")
        if city is None:
            raise ValueError("city cannot be None")
        if postal_code is None:
            raise ValueError("postal code cannot be None")
        if country is None:
            raise ValueError("country cannot be None")
        sql = """
        INSERT INTO Address(Street, StreetNumber, City, PostalCode, Country)
        VALUES (?, ?, ?, ?, ?)
        """
        params = tuple([street, street_number, city, postal_code, country])

        last_row_id, row_count = self.execute(sql, params)

        return model.Address(
            address_id=last_row_id,
            street=street,
            street_number=street_number,
            city=city,
            postal_code=postal_code,
            country=country)

    def show_address_by_id(self, address_id: int) -> model.Address | None:
        if address_id is None:
            raise ValueError("Address ID is required")
        sql = """ 
        SELECT 
            AddressId, 
            Street,
            StreetNumber,
            City,
            PostalCode,
            Country 
        FROM Address
        WHERE AddressId = ? 
            """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            (
                address_id,
                street,
                street_number,
                city,
                postal_code,
                country
            ) = result
            return model.Address(
                address_id,
                street,
                street_number,
                city,
                postal_code,
                country
            )
        else:
            return None
