import streamlit as st
from sql_connection import connect
import datetime
st.title("Please enter a booking number or a name")
col1, col2 = st.columns(2)


def showBooking():
    st.session_state.booking_number_input = ""
    st.session_state.given_name_input=""
    st.session_state.surname_input=""


    db=connect()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bookings b,guests g WHERE (b.booking_number=%s OR g.guest_given_name=%s AND g.guest_surname=%s) AND b.guest=g.person_id  ",
                   (
                       st.session_state["booking_number"],
                       st.session_state["given_name"],
                       st.session_state["surname"],

                   ))
    zeile_show=cursor.fetchone()
    db.commit()


    if zeile_show:
        st.session_state["data"] = zeile_show



with col1:
    st.session_state["booking_number"]=st.text_input("Booking Number",key="booking_number_input")
    st.button("Show booking",on_click=showBooking)
with col2:
    st.session_state["given_name"]=st.text_input("Given Name",key="given_name_input").lower()
    st.session_state["surname"]=st.text_input("Surname",key="surname_input").lower()
st.divider()

if "data" in st.session_state:
    data = st.session_state["data"]

    def showTotalNight():
        data = st.session_state["data"]

        nights=[x.strip() for x in data["total_nights_excl_discount"].split(',')]
        nights_date=[]
        for x in range(data["number_of_nights"]):
            date=data["check_in"]+datetime.timedelta(days=x)
            total_night=str(date)+": "+str(nights[x])
            nights_date.append(total_night)
        for x in range(len(nights_date)):
            st.write(nights_date[x])





    col3, col4 = st.columns(2)
    with col3:
        st.title("Booking Informations")
        st.write("Booking Number: "+str(data["booking_number"]))
        st.write("Number of guests: "+str(data["number_guests"]))
        st.write("Adults: "+str(data["adults"]))
        st.write("Kids: "+str(data["kids"]))
        st.write("Babies: "+str(data["babies"]))
        st.write("Pets: "+str(data["pets"]))
        st.write("Check-In: "+str(data["check_in"]))
        st.write("Check-Out: "+str(data["check_out"]))
        st.write("Nights stayed: "+str(data["number_of_nights"]))
        st.write("Date of booking: "+str(data["booking_date"]))
        st.write("Average price per night incl. discount: "+str(data["avg_ppn_incl_discount"]))
        st.write("Cleaning fee: "+str(data["cleaning_fee"]))
        st.write("Service fee for guests: "+str(data["service_fee_guest"]))
        st.write("Total paid: "+str(data["total_paid"]))
        if data["total_nights_excl_discount"]:
            st.write("Total per night excluding discounts: ")
            showTotalNight()
        st.write("Total discount: "+str(data["total_discount"]))
        st.write("Service fee for landlord: "+str(data["service_fee_landlord"]))
        st.write("Total received: "+str(data["total_received"]))
        if data["cancelled"]:
            st.write("Cancelled: Yes")
            st.write("Date of cancelled: "+str(data["date_of_cancel"]))
        else:
            st.write("Cancelled: No")
        st.write("Bed config: "+str(data["bed_config"]))
    with col4:
        st.title("Person Informations")
        st.write("Given name: "+str(data["guest_given_name"]).capitalize())
        st.write("Surname: "+str(data["guest_surname"]).capitalize())
        st.write("Rating: "+str(data["rating"]))
        st.write("Cleanliness: "+str(data["cleanliness"]))
        st.write("Houserules: "+str(data["houserules"]))
        st.write("Communication: "+str(data["communication"]))
        st.write("Number of travels: "+str(data["number_of_travels"]))
        st.write("Number of ratings: "+str(data["number_of_ratings"]))
        st.write("AirBnB member since: "+str(data["airbnb_member_since"]))
        st.write("Country of residence: "+data["country_of_residence"].capitalize())
        st.write("City of residence: "+data["city_of_residence"].capitalize())
        st.write("Nationality: "+data["nationality"].capitalize())
        st.write("Job: "+data["job"].capitalize())
        st.write("Email: "+data["email"])
        st.write("Age: "+data["age"])
        st.write("Comments: "+str(data["comments"]))
        if data["candidate_lastminute"]:
            st.write("Candidate for last minute offering: Yes")
        else:
            st.write("Candidate for last minute offering: No")


