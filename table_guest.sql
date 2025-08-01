CREATE TABLE guests (
    ID INT NOT NULL AUTO_INCREMENT,
    guest_name TINYTEXT,
    rating DEC,
    cleanliness DEC,
    houseroules DEC,
    communication DEC,
    number_of_travels INT,
    number_of_ratings INT,
    airbnb_member_since YEAR,
    country_of_residence VARCHAR(3000),
    city_of_residence TINYTEXT,
    nationality TINYTEXT,
    job TINYTEXT,
    email TINYTEXT,
    age INT,
    comments VARCHAR (3000),
    candiate_last_minute BOOL,
    bed_config TINYTEXT,
    PRIMARY KEY (ID)


);