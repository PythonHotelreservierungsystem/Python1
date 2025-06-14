import model
from model import Facility

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

# if __name__ == "__main__":
#     import os
#
#     # Pfad zur Datenbank setzen
#     db_path = os.path.join("..", "database", "hotel_reservation_sample.db")
#
#     # DataAccess-Instanz erstellen
#     facility_da = FacilityDataAccess(db_path)
#
#     # Beispielhafte Room-ID
#     test_room_id = 1
#
#     # Test: Facilities zu einem Zimmer laden
#     facilities = facility_da.get_facilities_by_room_id(test_room_id)
#
#     # Ausgabe
#     print(f"Ausstattung für Zimmer {test_room_id}:")
#     for f in facilities:
#         print(f"- {f.facility_name} (ID: {f.facility_id})")









    # def add_facility_to_room(self) -> list[Facility]:
    #     sql="""
    #     Select Facilities.facility_id, facility_name, Room_Facilities.room_id
    #     FROM Facilities
    #     JOIN Room_Facilities ON Facilities.facility_id = Room_Facilities.facility_id"""
    #
    #     facility_list = self.fetchall(sql)
    #     return_list = []
    #     for facility_id, facility_name, room_id in facility_list:
    #         return_list.append(
    #             Facility(
    #             facility_id=facility_id,
    #             facility_name=facility_name,
    #             room_id=RoomFacilities(room_id)
    #             )
    #         )
    #     return return_list


