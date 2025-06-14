from __future__ import annotations

class RoomFacilities:
    ##attributes#
    def __init__(self, facility_id: int, room_id: int):
        if not facility_id:
            raise ValueError("facility_id ist erforderlich")
        if not isinstance(facility_id, int):
            raise ValueError("facility_id muss eine Zahl sein")
        self.facility_id = facility_id
        self.room_id = room_id