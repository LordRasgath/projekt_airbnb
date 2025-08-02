import streamlit as st

homepage=st.Page(
    "pages/1_homepage.py",
    title="Homepage",
    url_path="homepage"
)
newbooking = st.Page(
    "pages/2_add_new_booking.py",
    title="Add a new Booking",
    url_path="new_booking")
visualize=st.Page(
    "pages/3_Visualize.py",
    url_path="visualize"
)
navigation = st.navigation([homepage,newbooking,visualize])
navigation.run()
