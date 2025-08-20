import streamlit as st
import pandas as pd
import calendar
import datetime
from sql_connection import connect
tab1,tab2,tab3=st.tabs(["Monthly revenue","Quarterly revenue","Yearly revenue"])
with tab1:
    currentDateTime = datetime.datetime.now()
    year = currentDateTime.date().year
    list_years = list(
        range(2020, year + 2))
    st.session_state["year"]=st.selectbox("Select Year",list_years,key="year_month")
    st.divider()
    db=connect()
    cursor=db.cursor()
    cursor.execute("""
    SELECT  MONTH(check_in) AS month_num, MONTHNAME(check_in) AS month, SUM(total_received) AS sum
    FROM bookings 
    WHERE YEAR(check_in)=%s 
    GROUP BY  month;"""
    ,(st.session_state["year"],))
    data=cursor.fetchall()

    monthly_revenue = pd.DataFrame(data, columns=["month_num", "month", "sum"])

    monthly_revenue["month"] = pd.Categorical(
        monthly_revenue["month"],
        categories=list(calendar.month_name)[1:],
        ordered=True
    )

    monthly_revenue = monthly_revenue.sort_values("month_num")
    monthly_revenue["sum"] = monthly_revenue["sum"].astype(float).round(2)

    st.bar_chart(monthly_revenue.set_index("month")["sum"])
with tab2:
    st.session_state["year_quarter"] = st.selectbox("Select Year", list_years)
    st.divider()
    cursor.execute("""
    SELECT QUARTER(check_in) AS quarter, SUM(total_received) AS sum
    FROM bookings 
    WHERE YEAR(check_in)=%s 
    GROUP BY quarter
    ORDER BY quarter;
    """,(st.session_state["year_quarter"],))
    data=cursor.fetchall()
    quarterly_revenue = pd.DataFrame(data, columns=["quarter", "sum"])
    quarterly_revenue["sum"] = quarterly_revenue["sum"].astype(float).round(2)
    st.bar_chart(quarterly_revenue.set_index("quarter")["sum"])

with tab3:
    cursor.execute("""
    SELECT YEAR(check_in) AS year, SUM(total_received) AS sum
    FROM bookings
    GROUP BY year
    ORDER BY year;
    """)
    data=cursor.fetchall()
    yearly_revenue=pd.DataFrame(data, columns=["year", "sum"])
    yearly_revenue["sum"]=yearly_revenue["sum"].astype(float).round(2)
    st.bar_chart(yearly_revenue.set_index("year")["sum"])