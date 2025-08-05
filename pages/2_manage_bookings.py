import os
import re
import sys

import pdfplumber as plumber
import streamlit as st

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # ability for Python to import from a parent folder
import datetime
from sql_connection import connect  # importing the database connector

tab1, tab2 = st.tabs(["Manually manage Booking", "Import Data from PDF"])
with tab1:
    st.title("Add a Person")
    currentDateTime = datetime.datetime.now()
    year = currentDateTime.date().year
    list_years = list(
        range(2008, year + 1))  # for AirBNB Member since: Ability to select the Year from 2008 until the current
    list_countries = list(
        ['', 'Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla',
         'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
         'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan',
         'Bolivia,', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island',
         'Brazil',
         'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia',
         'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China',
         'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
         'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba',
         'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
         'Egypt',
         'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands',
         'Fiji',
         'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia',
         'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
         'Guatemala',
         'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands',
         'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
         'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan',
         'Kenya',
         'Kiribati', 'Korea, South', "Kosovo", 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia',
         'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
         'North Macedonia',
         'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique',
         'Mauritania',
         'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco',
         'Mongolia',
         'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
         'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island',
         'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama',
         'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico',
         'Qatar',
         'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy',
         'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia',
         'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa',
         'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
         'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
         'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan',
         'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
         'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo',
         'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands',
         'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
         'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Viet Nam',
         'British Virgin Islands', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])
    col1, col2, col3 = st.columns(3, border=True)
    with col1:
        given_name = st.text_input("Given name (mandatory)", key="given_name", max_chars=255)
        houserules = st.number_input("Houserules", key="houserules", value=0.0, min_value=0.0, max_value=5.0,
                                     format="%0.1f", step=0.1)
        number_ratings = st.number_input("Total number of ratings", key="number_ratings", min_value=0)
        city_residence = st.text_input("City of residence", key="city_residence", max_chars=255)
        email = st.text_input("Email", key="email", max_chars=255)
        bed_config = st.text_input("Bed Configuration", key="bed_config", max_chars=255)

    with col2:
        surname = st.text_input("Surname", key="surname", max_chars=255)
        total_rating = st.number_input("Total Rating", key="total_rating", value=0.0, min_value=0.0, max_value=5.0,
                                       format="%0.1f", step=0.1)
        communication = st.number_input("Communication", key="communication", value=0.0, min_value=0.0, max_value=5.0,
                                        format="%0.1f", step=0.1)
        member_since = st.selectbox("AirBNB Member since", list_years, key="member_since")
        nationality = st.selectbox("Nationality", list_countries, key="nationality")
        phone = st.text_input("Phone Number", key="phone", max_chars=255)
        candidate_lastminute = st.checkbox("Candidate for last minute offering", key="candidate_lastminute",
                                           value=False)

    with col3:
        cleanliness = st.number_input("Cleanliness", key="cleanliness", value=0.0, min_value=0.0, max_value=5.0,
                                      format="%0.1f", step=0.1)
        number_travels = st.number_input("Total number of travels", key="number_travels", min_value=0)
        country = st.selectbox("Country of residence", list_countries, key="country")
        job = st.text_input("Job", key="job", max_chars=255)
        age = st.text_input("Approximate Age", key="age", max_chars=255)
        comments = st.text_area("Comments", key="comments")


    def addPerson():  # Function to add the Person to the Database, takes variables from the Inputs above
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO guests(guest_given_name, guest_surname, rating, cleanliness, houserules, communication, number_of_travels, number_of_ratings, airbnb_member_since, country_of_residence, city_of_residence, nationality, job, email, age, comments, candidate_lastminute, bed_config) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                given_name.lower(),
                surname.lower(),
                total_rating,
                cleanliness,
                houserules,
                communication,
                number_travels,
                number_ratings,
                member_since,
                country.lower(),
                city_residence.lower(),
                nationality.lower(),
                job.lower(),
                email.lower(),
                age.lower(),
                comments.lower(),
                candidate_lastminute,
                bed_config.lower()
            )
        )
        db.commit()


    def resetPerson():
        st.session_state.given_name = ""
        st.session_state.surname = ""
        st.session_state.total_rating = 0.0
        st.session_state.cleanliness = 0.0
        st.session_state.houserules = 0.0
        st.session_state.communication = 0.0
        st.session_state.number_travels = 0
        st.session_state.number_ratings = 0
        st.session_state.country = ""
        st.session_state.job = ""
        st.session_state.email = ""
        st.session_state.age = ""
        st.session_state.comments = ""
        st.session_state.candidate_lastminute = False
        st.session_state.bed_config = ""
        st.session_state.nationality = ""
        st.session_state.member_since = 2008
        st.session_state.country_of_residence = ""
        st.session_state.city_of_residence = ""


    def add_and_reset_person():
        addPerson()
        resetPerson()
        with col6:
            st.success("Successfully added a person to the database")


    col4, col5, col6 = st.columns([1, 1, 1])
    with col6:  # to make the button appear on the right without the borders from the first 3 columns above
        st.button("Add a Person to the Database", on_click=add_and_reset_person)

    st.divider()
    st.title("Add a Booking")
    col7, col8, col9 = st.columns(3, border=True)

    with col7:
        booking_number = st.text_input("Booking Number (mandatory)", key="booking_number", max_chars=10)
        kids = st.number_input("Number of kids", key="kids", min_value=0)
        check_in = st.date_input("Check In Date (mandatory)", key="check_in")
        booking_date = st.date_input("Booking Date (mandatory)", key="booking_date")
        service_fee_guests = st.number_input("Service fee for guests (mandatory)", min_value=0.00, format="%0.01f",
                                             key="service_fee_guests")
        total_discount = st.number_input("Total Discount", min_value=0.00, format="%0.01f", key="total_discount")
    with col8:
        number_guests = st.number_input("Number of guests (mandatory)", key="number_guests", min_value=0)
        babies = st.number_input("Number of babies", key="babies", min_value=0)
        check_out = st.date_input("Check Out Date (mandatory)", key="check_out")
        avg_ppn_incl_discount = st.number_input("Average Price per night, incl. discount (mandatory)", min_value=0.00,
                                                format="%0.01f", key="avg_ppn_incl_discount")
        total_paid = st.number_input("Total price paid (mandatory)", min_value=0.00, format="%0.01f", key="total_paid")
        service_fee_landlord = st.number_input("Service fee for landlord (mandatory)", min_value=0.00, format="%0.01f",
                                               key="service_fee_landlord")
    with col9:
        adults = st.number_input("Number of adults", min_value=0, key="adults")
        pets = st.number_input("Number of pets", min_value=0, key="pets")
        number_of_nights = st.number_input("Number of nights stayed (mandatory)", min_value=0, key="number_of_nights")
        cleaning_fee = st.number_input("Cleaning Fee", min_value=0.00, format="%0.01f", key="cleaning_fee")
        total_nights_excl_discount = st.number_input("Total nights excluding discount (mandatory)", min_value=0.00,
                                                     format="%0.01f", key="total_nights_excl_discount")
        total_received = st.number_input("Total received (mandatory)", min_value=0.00, format="%0.01f",
                                         key="total_received")

    col10, col11, col12 = st.columns(3)


    def addBooking():  # references booking to the last person pushed to database
        db = connect()
        cursor = db.cursor()
        cursor.execute("SELECT MAX(person_id) FROM guests")
        latest_person_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO bookings(booking_number,number_guests, adults, kids, babies, pets, check_in, check_out, number_of_nights, booking_date, avg_ppn_incl_discount, cleaning_fee, service_fee_guest, total_paid, total_nights_excl_discount, total_discount, service_fee_landlord, total_received,guest) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                booking_number,
                number_guests,
                adults,
                kids,
                babies,
                pets,
                check_in,
                check_out,
                number_of_nights,
                booking_date,
                avg_ppn_incl_discount,
                cleaning_fee,
                service_fee_guests,
                total_paid,
                total_nights_excl_discount,
                total_discount,
                service_fee_landlord,
                total_received,
                latest_person_id,

            )
        )
        db.commit()


    def resetBooking():
        st.session_state.booking_number = ""
        st.session_state.check_in = datetime.date.today()
        st.session_state.check_out = datetime.date.today()
        st.session_state.number_guests = 0
        st.session_state.kids = 0
        st.session_state.adults = 0
        st.session_state.pets = 0
        st.session_state.babies = 0
        st.session_state.number_of_nights = 0
        st.session_state.booking_date = datetime.date.today()
        st.session_state.avg_ppn_incl_discount = 0
        st.session_state.cleaning_fee = 0
        st.session_state.service_fee_guests = 0
        st.session_state.total_paid = 0
        st.session_state.total_nights_excl_discount = 0
        st.session_state.total_received = 0
        st.session_state.total_discount = 0
        st.session_state.service_fee_landlord = 0


    def addAndResetBooking():
        addBooking()
        resetBooking()
        with col12:
            st.success("Successfully added a booking to the database")


    with col12:
        st.button("Add a new Booking to the Database", on_click=addAndResetBooking)

    st.divider()
    st.title("Cancel a Booking")
    col13, col14, col15 = st.columns(3)


    def cancelBooking(cancel_date, booking_number):
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE bookings SET cancelled=true, date_of_cancel=%s WHERE booking_number=%s",
            (cancel_date, booking_number)
        )
        db.commit()
        with col15:
            st.success("Booking cancelled.")
        st.session_state.cancel_date = datetime.date.today()
        st.session_state.booking_number_cancel = ""


    with col13:
        booking_number = st.text_input("Booking Number", max_chars=10, key="booking_number_cancel")

    with col14:
        cancel_date = st.date_input("Date of cancellation", key="cancel_date")

    with col15:
        st.button("Cancel Booking", on_click=cancelBooking, args=(cancel_date, booking_number))




with tab2:
    uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")
if uploaded_pdf is not None:
    with plumber.open(uploaded_pdf) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"
        st.text_area("Extrahierter Text", all_text, height=300)

        booking_date_match = re.search(r"Booking date\s*\n?\s*([A-Za-z]{3},\s+[A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})",all_text)
        if booking_date_match:
            booking_date_str = booking_date_match.group(1)
            booking_date = datetime.datetime.strptime(booking_date_str, "%a, %b %d, %Y").date()
            st.write("Booking Date:", booking_date)

        checkin_match = re.search(r"Check-in\s*\n?\s*([A-Za-z]{3},\s+[A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})", all_text)
        if checkin_match:
            checkin_str = checkin_match.group(1)
            check_in = datetime.datetime.strptime(checkin_str, "%a, %b %d, %Y").date()
            st.write("Check-in:", check_in)

        checkout_match = re.search(r"Checkout\s*\n?\s*([A-Za-z]{3},\s+[A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})", all_text)
        if checkout_match:
            checkout_str = checkout_match.group(1)
            check_out = datetime.datetime.strptime(checkout_str, "%a, %b %d, %Y").date()
            st.write("Checkout:", check_out)

        guest_match = re.search(r"(\d+)\s+adults?,\s*(\d+)\s+(?:child|children|kids?)", all_text, re.IGNORECASE)
        if guest_match:
            adults = int(guest_match.group(1))
            kids = int(guest_match.group(2))
            st.write(f"Guests: {adults} Adults, {kids} Kids")

        number_match = re.search(r"Confirmation code\s*\n?\s*([A-Za-z0-9]{10})", all_text)
        if number_match:
            booking_number = number_match.group(1)
            st.write("Booking Number:", booking_number)

        guests_match = re.search(r"(\d+)\s+guests", all_text, re.IGNORECASE)
        number_guests = int(guests_match.group(1)) if guests_match else None
        st.write(f"Number of guests: {number_guests}")

        nights_match = re.search(r"\(\s*(\d+)\s+nights?\s*\)", all_text, re.IGNORECASE)
        number_of_nights = int(nights_match.group(1)) if nights_match else None
        st.write(f"Number of nights: {number_of_nights}")

        avg_ppn_match = re.search(r"Guest paid\s*\$\s*([\d,.]+)\s*x\s*\d+\s*nights", all_text, re.IGNORECASE)
        avg_ppn_incl_discount = float(avg_ppn_match.group(1).replace(",", "")) if avg_ppn_match else None
        st.write(f"Avg price per night incl. discount: {avg_ppn_incl_discount}")

        cleaning_fee_match = re.search(r"Cleaning fee \$([\d,.]+)", all_text, re.IGNORECASE)
        cleaning_fee = float(cleaning_fee_match.group(1).replace(",", "")) if cleaning_fee_match else 0.0
        st.write(f"Cleaning fee: {cleaning_fee}")

        service_fee_guests_match = re.search(r"Guest service fee \$([\d,.]+)", all_text, re.IGNORECASE)
        service_fee_guests = float(
            service_fee_guests_match.group(1).replace(",", "")) if service_fee_guests_match else 0.0
        st.write(f"Service fee guests: {service_fee_guests}")

        total_paid_match = re.search(r"Total \(USD\) \$([\d,.]+)", all_text, re.IGNORECASE)
        total_paid = float(total_paid_match.group(1).replace(",", "")) if total_paid_match else 0.0
        st.write(f"Total paid: {total_paid}")

        match = re.search(r"\w{3}, \d{2}/\d{2} \$([\d,.]+)", all_text)
        if match:
            total_nights_excl_discount = float(match.group(1).replace(",", ""))
        else:
            total_nights_excl_discount = None

        st.write("Total per night excluding discount:", total_nights_excl_discount)

        total_discount_match = re.search(r"Nightly rate adjustment\s*[−-]\$([\d,.]+)", all_text, re.IGNORECASE)
        total_discount = float(total_discount_match.group(1).replace(",", "")) if total_discount_match else 0.0
        st.write(f"Total discount: {total_discount}")

        service_fee_landlord_match = re.search(r"Host service fee.*[−-]\$([\d,.]+)", all_text, re.IGNORECASE)
        service_fee_landlord = float(
            service_fee_landlord_match.group(1).replace(",", "")) if service_fee_landlord_match else 0.0
        st.write(f"Service fee landlord: {service_fee_landlord}")

        lines = all_text.splitlines()

        if len(lines) >= 3:
            name_line = lines[2].strip()
            name_parts = name_line.split()


            given_name = name_parts[0]
            surname = " ".join(name_parts[1:])

            st.write("Given name:", given_name)
            st.write("Surname:", surname)

        rating_match = re.search(r"([0-9.]+)\s+rating", all_text)
        rating = rating_match.group(1) if rating_match else ""
        member_since_match = re.search(r"Airbnb in (\d{4})", all_text)
        airbnb_member_since = member_since_match.group(1) if member_since_match else ""
        location_line_match = re.search(r"Lives in (.+),\s*(.+)", all_text)
        city_of_residence = location_line_match.group(1).strip()
        country_of_residence = location_line_match.group(2).strip()
        st.write("Rating:", rating)
        st.write("Airbnb Member Since:", airbnb_member_since)
        st.write("City of residence:", city_of_residence)
        st.write("Country of residence:", country_of_residence)


    col1, col2 ,col3= st.columns(3)
    with col3:
        if st.button("Submit"):
            addBooking()