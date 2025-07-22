import streamlit as st
import datetime

st.title("Age calculator")
min_date = datetime.date(1900, 1, 1)
dob = st.date_input("Enter your dob",min_value=min_date, max_value=datetime.date.today())
today = datetime.date.today()
age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

st.text(f"You are {age_years} years old")