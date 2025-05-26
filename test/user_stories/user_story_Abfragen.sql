##User Story 1.4
       SELECT Hotel.hotel_id, Hotel.name, COUNT(Room.room_id) AS available_rooms
FROM Hotel
JOIN Room ON Room.hotel_id = Hotel.hotel_id
LEFT JOIN Booking ON Booking.room_id = Room.room_id
    AND NOT (
        Booking.check_out_date <= ?
        OR Booking.check_in_date >= ?
    )
WHERE Booking.booking_id IS NULL
GROUP BY Hotel.hotel_id, Hotel.name

