import streamlit as st

st.header("st.button")

button = st.button("say hello")

if button:
    st.write("hello there!")
else:
    st.write("goooby")