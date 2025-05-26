#User Story 1.4
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
ON Room.type_id = Room_Type.type_id

LEFT JOIN Booking
ON Booking.room_id = Room.room_id
    AND NOT (
        Booking.check_out_date <= ?
        OR Booking.check_in_date >= ?
    )
WHERE
    Booking.booking_id IS NULL
    AND Hotel.stars >= 5
    AND Room_Type.max_guests >= 2



#User Story 1.6
SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.street, Address.zip_code, Address.city
FROM Hotel

JOIN
Address
ON Hotel.address_id = Address.address_id

#User Story 2

SELECT
Hotel.hotel_id,
Hotel.name,
Hotel.stars,
Address.address_id,
Address.street,
Address.zip_code,
Address.city,
Room.room_id,
Room.price_per_night,
Room_Type.max_guests,
Room_Type.description,
Room_Facilities.facility_id

FROM
Hotel

JOIN
Address
ON Hotel.address_id = Address.address_id

JOIN
Room_Type
ON Room_Type.type_id = Room.type_id

JOIN
Room
ON Room.hotel_id = Hotel.hotel_id

JOIN
Room_Facilities
ON Room_Facilities.room_id = Room.room_id

#User Story 2.1 (muss evtl. noch angepasst werden mit +1 booking_id)

SELECT
    Room.room_id,
    Room.price_per_night,
    Room_Type.type_id,
    Room_Type.max_guests,
    Room_Type.description,
    Booking.booking_id,
    Booking.total_amount,
    Facilities.facility_name

FROM
Room
JOIN
Booking
ON
Booking.room_id = Room.room_id

JOIN
Room_Type
ON
Room.type_id = Room_Type.type_id

JOIN
Room_Facilities
ON
Room_Facilities.room_id = Room.room_id

JOIN
Facilities
ON
Room_Facilities.facility_id = Facilities.facility_id




