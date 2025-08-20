import streamlit as st

homepage=st.Page(
    "pages/1_homepage.py",
    title="Homepage",
    url_path="homepage"
)
newbooking = st.Page(
    "pages/2_manage_bookings.py",
    title="Manage Bookings",
    url_path="manage_bookings")
visualize=st.Page(
    "pages/5_Visualize.py",
    url_path="visualize"
)
update=st.Page(
    "pages/3_update.py",
    title="Update Bookings/Persons",
    url_path="update"
)
showBooking=st.Page(
    "pages/4_show_booking.py",
    title="Show a Booking",
    url_path="show_booking"

)
navigation = st.navigation([homepage,newbooking,update,showBooking,visualize])
navigation.run()
