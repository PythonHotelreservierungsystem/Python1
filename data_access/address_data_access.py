from __future__ import annotations

import model

from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
##Do müend bi de Models no ergänzt werde mit Country und so u
    def create_address(
            self,
            street: str,
            city: str,
            zip_code: str
    ) -> model.Address:
        if street is None:
            raise ValueError("street cannot be None")
        if city is None:
            raise ValueError("city cannot be None")
        if zip_code is None:
            raise ValueError("postal code cannot be None")
        sql = """
        INSERT INTO Address(Street, City, Zip_Code)
        VALUES (?, ?, ?)
        """
        params = tuple([street, city, zip_code])

        last_row_id, row_count = self.execute(sql, params)

        return model.Address(
            address_id=last_row_id,
            street=street,
            city=city,
            zip_code=zip_code
        )


    def show_address_by_id(self, address_id: int) -> model.Address | None:
        if address_id is None:
            raise ValueError("Address ID is required")
        sql = """ 
        SELECT 
            Address_Id, 
            Street,
            City,
            Zip_Code 
        FROM Address
        WHERE Address_Id = ? 
            """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            (
                address_id,
                street,
                city,
                zip_code
            ) = result
            return model.Address(
                address_id,
                street,
                city,
                zip_code
            )
        else:
            return None
