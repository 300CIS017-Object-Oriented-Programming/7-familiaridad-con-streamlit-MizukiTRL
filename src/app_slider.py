import streamlit as st
from datetime import datetime, time

st.title("st.slider")

st.subheader("slider")

age = st.slider("how old are you: ", 0, 120, 18)

st.write("I am", age, "years old")

st.subheader("Range slidder")

values = st.slider(
    "select a range of values",
    0.0, 100.0, (25.0, 75.0)
)

st.write("values: ", values)

st.subheader("time slider")

appointment = st.slider(
    "select an appointment",
    value = (time(11, 30), time(12, 45))
)

st.write("appointment: ", appointment)

st.subheader("Date time slider")

start_time = st.slider(
    "when is it starting",
    value = datetime(2024, 4, 22, 16, 30),
    format="MM/DD/YY - hh:mm"
)

st.write("start time: ", start_time)