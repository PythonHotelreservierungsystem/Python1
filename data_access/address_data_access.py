from __future__ import annotations

from multiprocessing.util import spawnv_passfds

import model

from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


##Do müend bi de Models no ergänzt werde mit Country und so u
    def create_address(self,street: str,city: str,zip_code: int) -> model.Address:

        if street is None:
            raise ValueError("street cannot be None")
        if city is None:
            raise ValueError("city cannot be None")
        if zip_code is None:
            raise ValueError("zip code cannot be None")
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

    #delete Addresss
    def delete_address(self,address: model.Address):
        pass

    #update Address
    def update_address(self, address_id: int, street: str, city: str, zip_code: int) -> bool:
        sql = """
              UPDATE Address SET street   = ?, city     = ?, zip_code = ? WHERE address_id = ? \
              """
        params = (street, city, zip_code, address_id)
        _, row_count = self.execute(sql, params)
        return row_count > 0


    #adressse nach id ahzeige
    def show_address_by_id(self, address_id: int) -> model.Address | None:
        if address_id is None:
            raise ValueError("Address ID is required")
        sql = """ 
        SELECT 
        Address_Id,Street,City,Zip_Code FROM Address WHERE Address_Id = ? 
            """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            (address_id,street,city,zip_code) = result
            return model.Address(
                address_id,street,city,int(zip_code))
        else:
            return None
