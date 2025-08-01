CREATE TABLE guests (
    person_ID INT NOT NULL AUTO_INCREMENT,
    guest_name TINYTEXT,
    rating DEC(1,1),
    cleanliness DEC(1,1),
    houseroules DEC(1,1),
    communication DEC(1,1),
    number_of_travels INT,
    number_of_ratings INT,
    airbnb_member_since YEAR,
    country_of_residence TINYTEXT,
    city_of_residence TINYTEXT,
    nationality TINYTEXT,
    job TINYTEXT,
    email TINYTEXT,
    age INT,
    comments VARCHAR (3000),
    candiate_last_minute BOOL,
    bed_config TINYTEXT,
    PRIMARY KEY (person_ID)


);