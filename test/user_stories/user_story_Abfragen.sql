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

User Story 1.5
SELECT
    Hotel.hotel_id,
    Hotel.name,
    Hotel.stars,
    Address.address_id,
    Room.room_id,
    Room.room_number,
    Room_Type.type_id,
    Room_Type.max_guests
FROM
    Hotel
JOIN Address
ON Hotel.address_id = Address.address_id

JOIN Room
ON Room.hotel_id = Hotel.hotel_id

JOIN Room_Type
ON Room_Type.type_id = Room_Type.type_id

LEFT JOIN Booking
ON Booking.room_id = Room.room_id
    AND NOT (
        Booking.check_out_date <= ?
        OR Booking.check_in_date >= ?
    )
WHERE
    Booking.booking_id IS NULL
    AND Hotel.stars >= ?
    AND Room_Type.max_guests >= ?
    AND Address.city = ?
ORDER BY
    Hotel.name,
    Room.room_number

##User Story 1.6
SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.street, Address.zip_code, Address.city
FROM Hotel

JOIN
Address
ON Hotel.address_id = Address.address_id


