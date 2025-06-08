import model
from datetime import date
from data_access.base_data_access import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

##User Story 4
    def create_booking(self, guest_id: model.Guest = None, room_id: model.Room = None, check_in_date: date =None, check_out_date: date = None, is_cancelled: bool = False, total_amount: float = 0.0
    ) -> model.Booking:
        if check_in_date is None or check_out_date is None:
            raise ValueError("Check in and check out dates are required")
        if check_in_date > check_out_date:
            raise ValueError("Check in date cannot be after check out date")
        ##Für Userstory
        sql="""
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?,?,?,?,?,?)
            """

        params = tuple([
            guest_id.guest_id if guest_id else None,
            room_id.room_id if room_id else None,
            check_in_date,
            check_out_date,
            is_cancelled,
            total_amount
        ])

        last_row_id, row_count = self.execute(sql, params)
        return model.Booking(
            booking_id=last_row_id,
            hotel_id=room_id.hotel.hotel_id if room_id else None,
            room_id=room_id.room_id if room_id else None,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            is_cancelled=is_cancelled,
            total_amount=total_amount,
            guest=guest_id.guest_id if guest_id else None
        )
    def delete_booking_by_id(self, booking_id: int) -> bool:
        if booking_id is None:
            raise ValueError("booking_id darf nicht None sein")
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        params = (booking_id,)
        _, row_count = self.execute(sql, params)
        return row_count > 0

    ##User story 1.4 ? 2.2
    def show_bookings_with_hotels(self)-> list[model.Booking]:
        sql="""
        SELECT booking.booking_id, booking.room_id, booking.guest_id, booking.check_in_date, booking.check_out_date, booking.is_cancelled, booking.total_amount, room.hotel_id, room.room_number
        FROM Booking AS booking
        JOIN Room AS room ON booking.room_id = room.room_id
        """
        bookings = self.fetchall(sql)
        return_list = []
        for booking_id, room_id, guest_id, check_in_date, check_out_date, is_cancelled, total_amount, hotel_id, room_number in bookings:
            return_list.append(
                model.Booking(
                booking_id=booking_id,
                room_id=room_id,
                guest_id=guest_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                is_cancelled=is_cancelled,
                total_amount=total_amount,
                hotel_id=hotel_id
            )
        )
        return return_list
    #User Story 5
    def update_booking_by_id(self, booking_id: int, guest: model.Guest, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: int)-> bool:
        sql="""
        UPDATE Booking 
        SET guest_id = ?, check_in_date = ?, check_out_date = ?, is_cancelled = ?, total_amount = ? 
        WHERE booking_id = ?"""
        params = (guest, check_in_date, check_out_date, is_cancelled, total_amount, booking_id)
        _, row_count = self.execute(sql, params)
        return row_count > 0

    def cancel_booking(self, booking_id: int)-> bool:
        sql="""
        UPDATE Booking 
        SET is_cancelled = 1 
        WHERE booking_id = ?"""
        params = (booking_id,)
        _, row_count = self.execute(sql, params)
        return row_count > 0

