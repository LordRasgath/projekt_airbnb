import streamlit as st
from sql_connection import connect
import datetime

tab1,tab2 = st.tabs(["Update a Booking","Update a Person"])
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


def updateBooking():
    db = connect()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE bookings SET number_guests=%s,adults=%s,kids=%s,babies=%s,pets=%s,check_in=%s,check_out=%s,number_of_nights=%s,booking_date=%s,avg_ppn_incl_discount=%s,cleaning_fee=%s,service_fee_guest=%s,total_paid=%s,total_nights_excl_discount=%s,total_discount=%s,service_fee_landlord=%s,total_received=%s, bed_config=%s WHERE booking_number=%s",
        (
            st.session_state["number_guests"],
            st.session_state["adults"],
            st.session_state["kids"],
            st.session_state["babies"],
            st.session_state["pets"],
            st.session_state["check_in"],
            st.session_state["check_out"],
            st.session_state["number_of_nights"],
            st.session_state["booking_date"],
            st.session_state["avg_ppn_incl_discount"],
            st.session_state["cleaning_fee"],
            st.session_state["service_fee_guest"],
            st.session_state["total_paid"],
            st.session_state["total_nights_excl_discount"],
            st.session_state["total_discount"],
            st.session_state["service_fee_landlord"],
            st.session_state["total_received"],
            st.session_state["bed_config"],
            st.session_state["booking_number"],))
    db.commit()
    del st.session_state["booking_data"]
    st.session_state.booking_number=""
    st.success("Sucessfully updated booking")

def updatePerson():
    db = connect()
    cursor = db.cursor()
    cursor.execute("UPDATE guests SET rating=%s, cleanliness=%s, houserules=%s,communication=%s,number_of_travels=%s,number_of_ratings=%s,airbnb_member_since=%s,country_of_residence=%s,city_of_residence=%s,nationality=%s,job=%s,email=%s,age=%s,phone=%s,comments=%s,candidate_lastminute=%s WHERE guest_given_name=%s AND guest_surname=%s",(
        st.session_state["rating"],
        st.session_state["cleanliness"],
        st.session_state["houserules"],
        st.session_state["communication"],
        st.session_state["number_of_travels"],
        st.session_state["number_of_ratings"],
        st.session_state["airbnb_member_since"],
        st.session_state["country_of_residence"].lower(),
        st.session_state["city_of_residence"].lower(),
        st.session_state["nationality"].lower(),
        st.session_state["job"].lower(),
        st.session_state["email"],
        st.session_state["age"],
        st.session_state["phone"],
        st.session_state["comments"],
        st.session_state["candidate_lastminute"],
        st.session_state["given_name"].lower(),
        st.session_state["surname"].lower()))
    db.commit()
    del st.session_state["guest_data"]
    st.session_state.given_name=""
    st.session_state.surname=""

    st.success("Sucessfully updated guest")
with tab1:
    # Erste Zeile: Booking Number + Button
    col1, col2 = st.columns([2, 1])
    with col1:
        booking_number = st.text_input("Booking Number", key="booking_number")
    with col2:
        get_booking = st.button("Get Booking")


    if get_booking:
        db = connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bookings WHERE booking_number=%s", (booking_number,))
        zeile_booking = cursor.fetchone()
        db.commit()

        if zeile_booking:
            st.session_state["booking_data"] = zeile_booking


    if "booking_data" in st.session_state:
        zeile = st.session_state["booking_data"]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.session_state["number_guests"] = st.number_input("Number of guests", value=zeile["number_guests"])
            st.session_state["babies"] = st.number_input("Number of babies", value=zeile["babies"])
            st.session_state["check_out"] = st.date_input("Check-Out Date", value=zeile["check_out"])
            st.session_state["avg_ppn_incl_discount"] = st.number_input("Average P.p.N including discount",value=zeile["avg_ppn_incl_discount"], format="%.01f")
            st.session_state["total_paid"] = st.number_input("Total price paid", value=zeile["total_paid"])
            st.session_state["service_fee_landlord"]= st.number_input("Service Fee for landlord", value=zeile["service_fee_landlord"])

        with col2:
            st.session_state["adults"] = st.number_input("Number of adults", value=zeile["adults"])
            st.session_state["pets"] = st.number_input("Number of pets", value=zeile["pets"])
            st.session_state["number_of_nights"] = st.number_input("Number of nights", value=zeile["number_of_nights"])
            st.session_state["cleaning_fee"]= st.number_input("Cleaning Fee", value=zeile["cleaning_fee"],format="%.01f")
            st.session_state["total_nights_excl_discount"]=st.text_area("Prices per night excluding discount", value=zeile["total_nights_excl_discount"])
            st.session_state["total_received"]=st.number_input("Total money received", value=zeile["total_received"],format="%.01f")

        with col3:
            st.session_state["kids"] = st.number_input("Number of kids", value=zeile["kids"])
            st.session_state["check_in"] = st.date_input("Check-In Date", value=zeile["check_in"])
            st.session_state["booking_date"] = st.date_input("Booking Date", value=zeile["booking_date"])
            st.session_state["service_fee_guest"]=st.number_input("Service Fee for guests", value=zeile["service_fee_guest"],format="%.01f")
            st.session_state["total_discount"]=st.number_input("Total Discount", value=zeile["total_discount"],format="%.01f")
            st.session_state["bed_config"]=st.text_input("Bed Config", value=zeile["bed_config"],max_chars=255)

            st.button("Update Booking",on_click=updateBooking)
with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        given_name=st.text_input("Given Name", key="given_name").lower()
    with col2:
        surname=st.text_input("Surname", key="surname").lower()
    with col3:
        if st.button("Get Person"):
            db=connect()
            cursor=db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM guests WHERE guest_given_name=%s AND guest_surname=%s", (given_name.lower(),surname.lower()))
            zeile_person = cursor.fetchone()
            if zeile_person:
                st.session_state["guest_data"] = zeile_person
    if "guest_data" in st.session_state:
        zeile_person = st.session_state["guest_data"]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.session_state["rating"]=st.number_input("Rating", value=float(zeile_person["rating"]),format="%.1f")
            st.session_state["communication"]=st.number_input("Communication", value=float(zeile_person["communication"]),format="%.1f")
            st.session_state["airbnb_member_since"]=st.selectbox("AirBnB Member since",list_years,index=list_years.index(zeile_person["airbnb_member_since"]))
            st.session_state["nationality"]=st.selectbox("Nationality",list_countries,index=list_countries.index(zeile_person["nationality"].capitalize()))
            st.session_state["age"]=st.text_input("Approximate age", value=zeile_person["age"],max_chars=255)
            st.session_state["candidate_lastminute"]=st.checkbox("Candidate for last minute offering", value=zeile_person["candidate_lastminute"])

        with col2:
            st.session_state["cleanliness"]=st.number_input("Cleanliness", value=float(zeile_person["cleanliness"]),format="%.1f")
            st.session_state["number_of_travels"]=st.number_input("Number of travels", value=zeile_person["number_of_travels"])
            st.session_state["country_of_residence"]=st.selectbox("Country of Residence",list_countries,index=list_countries.index(zeile_person["country_of_residence"].capitalize()))
            st.session_state["job"]=st.text_input("Job", value=zeile_person["job"].capitalize(),max_chars=255)
            st.session_state["phone"]=st.text_input("Phone number", value=zeile_person["phone"],max_chars=255)
            st.session_state["comments"]=st.text_area("Comments", value=zeile_person["comments"])
        with col3:
            st.session_state["houserules"]=st.number_input("Houserules", value=float(zeile_person["houserules"]),format="%.1f")
            st.session_state["number_of_ratings"]=st.number_input("Number of ratings", value=zeile_person["number_of_ratings"])
            st.session_state["city_of_residence"]=st.text_input("City of residence", value=zeile_person["city_of_residence"].capitalize(),max_chars=255)
            st.session_state["email"]=st.text_input("Email", value=zeile_person["email"],max_chars=255)
            st.button("Update Guest",on_click=updatePerson)
