CREATE TABLE bookings(
    booking_number TINYTEXT NOT NULL,
    number_guests INT,
    adults INT,
    kids INT,
    babies INT,
    pets INT,
    check_in DATE,
    check_out DATE,
    number_of_nights INT,
    booking_date DATE,
    ppn_avg_w/discount FLOAT(24),
    cleaning_fee FLOAT(24),
    service_fee FLOAT(24),
    total_paid FLOAT(24),
    total_nights_w/o_discount FLOAT(24),
    total_discount FLOAT(24),
    service_fee_renter FLOAT(24),
    guest INT,
    PRIMARY KEY(booking_number)
    FOREIGN KEY (guest) REFERENCES guests(person_ID)
)