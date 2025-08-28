import streamlit as st
# Key file, this file specifies all pages and links to them
homepage=st.Page(
    "pages/1_homepage.py", #file path
    title="Homepage", #Title, relevant for example for the sidebar
    url_path="homepage" #name that displays in the browser URL
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
navigation = st.navigation([homepage,newbooking,update,showBooking,visualize]) #Adds an automatic sidebar
navigation.run()
