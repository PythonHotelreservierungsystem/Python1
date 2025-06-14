import model
from model import Facility

from data_access.base_data_access import BaseDataAccess


class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    #Hilfsfunktion
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

    ##User Story 2.1,
    def get_facilities_by_room_id(self, room_id: int) -> list[Facility]:
        sql = """
        SELECT f.facility_id, f.facility_name
        FROM Room_Facilities rf
        JOIN Facilities f ON rf.facility_id = f.facility_id
        WHERE rf.room_id = ? \
        """
        rows = self.fetchall(sql, (room_id,))
        return [Facility(facility_id=int(row[0]), facility_name=row[1]) for row in rows]