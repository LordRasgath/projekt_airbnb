import streamlit as st
from sql_connection import connect

tab1,tab2 = st.tabs(["Update a Booking","Update a Person"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        booking_number=st.text_input("Booking Number",)
    with col3:
        if st.button("Get Booking"):
            cursor=connect().cursor()
            cursor.execute("SELECT * FROM bookings WHERE booking_number=%s",(booking_number,))
