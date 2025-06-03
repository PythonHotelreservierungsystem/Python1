import model
from datetime import date
from data_access.base_data_access import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_booking(self,
                       guest_id: model.Guest = None,
                       room_id: model.Room = None,
                       check_in_date: date =None,
                       check_out_date: date = None,
                       is_cancelled: bool = False,
                       total_amount: float = 0.0
    ) -> model.Booking:
        if check_in_date is None or check_out_date is None:
            raise ValueError("Check in and check out dates are required")
        if check_in_date > check_out_date:
            raise ValueError("Check in date cannot be after check out date")
        ##Für Userstory
        sql="""
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?,?,?,?,?,?)"""

        params = tuple([
            Guest.guest_id if guest_id else None,
            Room.room_id if room_id else None,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        ])

        last_row_id, row_count = self.execute(sql, params)
        return model.Booking(
            booking_id=last_row_id,
            guest=guest_id,
            room=room_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            is_cancelled=is_cancelled,
            total_amount=total_amount
        )
    ##User story 3.8
    def show_bookings_with_hotels(self)-> list[model.Booking]:
        sql="""
        SELECT booking.booking_id, booking.room_id, booking.guest_id, booking.check_in_date, booking.check_out_date, booking.is_cancelled, booking.total_amount, room.hotel_id, room.room_number
        FROM Booking AS booking
        JOIN Room AS room ON booking.room_id = room.room_id
        """
        result = self.fetchall(sql)

        if result:
            bookings = []
            for row in result:
                (
                    booking_id,
                    room_id,
                    guest_id,
                    check_in_date,
                    check_out_date,
                    is_cancelled,
                    total_amount,
                    hotel_id,
                    room_number
                ) = row

                booking = model.Booking(
                    booking_id=str(booking_id),
                    room_id=room_id,
                    guest=guest_id,
                    check_in_date=check_in_date,
                    check_out_date=check_out_date,
                    is_cancelled=is_cancelled,
                    total_amount=total_amount,
                    hotel_id=hotel_id,

                )

            return bookings

        return []



