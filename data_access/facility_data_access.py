import model

from data_access.base_data_access import BaseDataAccess


class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_facility(
            self,
            facility_name: str
    ) -> model.Facility:
        if facility_name is None:
            raise ValueError("facility_name cannot be None")

        sql="""
        INSERT INTO Facilities (Facility_Name)
        VALUES (?)"""

        params =(facility_name,)

        last_row_id, row_count = self.execute(sql, params)

        return model.Facility(
        facility_id=last_row_id,
        facility_name=facility_name
    )