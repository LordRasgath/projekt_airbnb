import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #ability for Python to import from a parent folder
import datetime
from sql_connection import connect #importing the database connector
st.title("Add a Person")
currentDateTime = datetime.datetime.now()
year = currentDateTime.date().year
list_years=list(range(2008,year+1))# for AirBNB Member since: Ability to select the Year from 2008 until the current
list_countries=list(['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia,', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, South',"Kosovo", 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'North Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Viet Nam', 'British Virgin Islands', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])
col1,col2,col3=st.columns(3,border=True)
with col1:
    given_name=st.text_input("Given name (mandatory)",max_chars=255)
    houserules=st.number_input("Houserules",value=0.0,min_value=0.0,max_value=5.0,format="%0.1f",step=0.1)
    number_ratings=st.number_input("Total number of ratings",min_value=0)
    city_residence=st.text_input("City of residence",max_chars=255)
    email=st.text_input("Email",max_chars=255)
    bed_config=st.text_input("Bed Configuration",max_chars=255)

with col2:
    surname=st.text_input("Surname",max_chars=255)
    total_rating=st.number_input("Total Rating",value=0.0,min_value=0.0,max_value=5.0,format="%0.1f",step=0.1)
    communication=st.number_input("Communication",value=0.0,min_value=0.0,max_value=5.0,format="%0.1f",step=0.1)
    member_since=st.selectbox("AirBNB Member since",list_years)
    nationality=st.selectbox("Nationality",list_countries)
    phone=st.text_input("Phone Number",max_chars=255)
    candidate_lastminute=st.checkbox("Candidate for last minute offering",value=False)

with col3:
    cleanliness=st.number_input("Cleanliness",value=0.0,min_value=0.0,max_value=5.0,format="%0.1f",step=0.1)
    number_travels=st.number_input("Total number of travels",min_value=0)
    country=st.text_input("Country of residence",max_chars=255)
    job=st.text_input("Job",max_chars=255)
    age=st.text_input("Approximate Age",max_chars=255)
    comments=st.text_area("Comments")

def addPerson(): #Function to add the Person to the Database, takes variables from the Inputs above
    db=connect()
    cursor=db.cursor()
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
col4, col5, col6=st.columns([1,1,1])
with col6: #to make the button appear on the right without the borders from the first 3 columns above
    if st.button("Add a Person to the Database"):
        addPerson()
st.divider()
st.title("Add a Booking")
col7, col8, col9 = st.columns(3,border=True)

with col7:
    booking_number=st.text_input("Booking Number",max_chars=10)
    kids=st.number_input("Number of kids",min_value=0)
    check_in=st.date_input("Check In Date")
    booking_date=st.date_input("Booking Date")
    service_fee_guests=st.number_input("Service fee for guests",min_value=0.00,format="%0.01f")
    total_discount=st.number_input("Total Discount",min_value=0.00,format="%0.01f")
with col8:
    number_guests=st.number_input("Number of guests",min_value=0)
    babies=st.number_input("Number of babies",min_value=0)
    check_out=st.date_input("Check Out Date")
    avg_ppn_incl_discount=st.number_input("Average Price per night, incl. discount",min_value=0.00,format="%0.01f")
    total_paid=st.number_input("Total price paid",min_value=0.00,format="%0.01f")
    service_fee_landlord=st.number_input("Service fee for landlord",min_value=0.00,format="%0.01f")
with col9:
    adults=st.number_input("Number of adults",min_value=0)
    pets=st.number_input("Number of pets",min_value=0)
    number_of_nights=st.number_input("Number of nights stayed",min_value=0)
    cleaning_fee=st.number_input("Cleaning Fee",min_value=0.00, format="%0.01f")
    total_nights_excl_discount=st.number_input("Total nights excluding discount",min_value=0.00,format="%0.01f")
    total_received=st.number_input("Total received",min_value=0.00,format="%0.01f")

