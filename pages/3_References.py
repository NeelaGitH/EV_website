import streamlit as st
import pandas as pd

st.title("References")

st.header("Data for Charging Hour Prediction")
st.write("Source:", "https://www.kaggle.com/datasets/valakhorasani/electric-vehicle-charging-patterns")
data_charge = pd.read_csv(r"data\ev_charging_patterns.csv")
st.write(data_charge)


st.header("Data for Electric Vehicle Recommendation")
st.write("Source:", "https://www.kaggle.com/datasets/sahirmaharajj/electric-vehicle-population/data")
data_ev = pd.read_csv(r"data\Electric_Vehicle_Population_Data.csv")
st.write(data_ev)