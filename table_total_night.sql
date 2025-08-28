CREATE TABLE night_booked(
    date DATE,
    total_price_excl_discount float,
    discount float,
    cleaning_fee float,
    guest_service_fee float,
    host_service_fee float,
    total_revenue float,
    booking_number char(10),
    FOREIGN KEY (booking_number) REFERENCES bookings(booking_number),
    PRIMARY KEY (date)
)