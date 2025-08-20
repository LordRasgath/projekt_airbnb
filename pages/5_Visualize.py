import streamlit as st
import pandas as pd
import calendar
from sql_connection import connect
tab1,tab2,tab3=st.tabs(["Monthly revenue","Quarterly revenue","Yearly revenue"])
with tab1:
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT  MONTH(booking_date) AS monat, SUM(total_received) AS summe FROM bookings WHERE booking_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) GROUP BY  MONTH(booking_date) ORDER BY monat;")
    data=cursor.fetchall()
    monthly_revenue=pd.DataFrame(data,columns=["month","sum"])
    st.bar_chart(monthly_revenue.set_index("month")["sum"])