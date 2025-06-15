import pandas as pd

from data_access.booking_data_access import BookingDataAccess
from data_access.room_data_access import RoomDataAccess


class BookingAnalyticsManager:
    def __init__(self, booking_da: BookingDataAccess, room_da: RoomDataAccess):
        self.booking_da = booking_da
        self.room_da = room_da

    #Methode für Datenvisualisierung 1: Buchungen pro Zimmerart anzeigen lassen
    def get_booking_counts_by_room_type(self) -> pd.DataFrame:
        # Daten laden
        bookings = self.booking_da.show_bookings_with_hotels()
        rooms = self.room_da.show_room_details()

        # DataFrames erstellen
        df_bookings = pd.DataFrame([{
            "booking_id": b.booking_id,
            "room_id": b.room_id,
            "is_cancelled": b.is_cancelled
        } for b in bookings])

        df_rooms = pd.DataFrame([{
            "room_id": r.room_id,
            "room_type": r.room_type.description
        } for r in rooms])

        # Join über room_id
        df_merged = pd.merge(df_bookings, df_rooms, on="room_id", how="left")

        # Stornierte buchungen aussortieren
        df_valid = df_merged[df_merged["is_cancelled"] == 0]

        # Gruppieren und zählen
        df_counts = df_valid.groupby("room_type").size().reset_index(name="Anzahl_Buchungen")
        return df_counts