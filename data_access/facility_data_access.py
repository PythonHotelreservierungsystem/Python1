import model

from data_access.base_data_access import BaseDataAccess
from model import Facility, RoomFacilities


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
    ##Zusatz Data Access für Ausstattung
    def add_facility_to_room(self) -> list[Facility]:
        sql="""
        Select Facilities.facility_id, facility_name, Room_Facilities.room_id
        FROM Facilities
        JOIN Room_Facilities ON Facilities.facility_id = Room_Facilities.facility_id"""

        facility_list = self.fetchall(sql)
        return_list = []
        for facility_id, facility_name, room_id in facility_list:
            return_list.append(
                Facility(
                facility_id=facility_id,
                facility_name=facility_name,
                room_id=RoomFacilities(room_id)
                )
            )
        return return_list


if __name__ == "__main__":

    def test_add_facility_to_room():
        room_manager = FacilityDataAccess()
        db_path = "../database/hotel_reservation_sample.db"
        try:
            facilities = room_manager.add_facility_to_room()

            # Debug-Ausgabe der Rückgabewerte
            print("\n--- Rückgabewerte von add_facility_to_room() ---")
            for facility in facilities:
                print(
                    f"Facility-ID: {facility.facility_id}, Name: {facility.facility_name}, Room-ID: {facility.room_id.room_id}")

            # Zusätzliche Tests
            assert isinstance(facilities, list), "Rückgabe ist keine Liste"
            for facility in facilities:
                assert isinstance(facility, Facility), "Element ist kein Facility-Objekt"
                assert hasattr(facility, 'facility_id'), "facility_id fehlt"
                assert hasattr(facility, 'facility_name'), "facility_name fehlt"
                assert hasattr(facility, 'room_id'), "room_id fehlt"
                assert isinstance(facility.room_id, RoomFacilities), "room_id ist kein RoomFacilities-Objekt"

            print("\n✅ Test erfolgreich: Alle Facilities korrekt geladen und strukturiert.")

        except Exception as e:
            print(f"\n❌ Test fehlgeschlagen: {e}")


    test_add_facility_to_room()