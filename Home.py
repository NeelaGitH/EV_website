import streamlit as st
st.set_page_config(page_title="Home Page")

st.title("Welcome to our website")

st.write("Use our various functionalities")

if st.button("Charging Hours Prediction"):
    st.switch_page("pages/1_Charging_Hours_Prediction.py")
if st.button("EV_Recommender"):
    st.switch_page("pages/2_EV_Recommender.py")
if st.button("References"):
    st.switch_page("pages/3_References.py")

