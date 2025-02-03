import streamlit as st
import pickle
import pandas as pd

with open(r"models\model_ev.pkl", "rb") as file:
    model = pickle.load(file)

with open(r"pipelines\pipeline_ev.pkl", "rb") as file:
    pipeline = pickle.load(file)

st.title("Electric Car Model Recommender")

form_values = {
    "Model Year": None,
    "Electric Vehicle Type": None,
    "Electric Range" : None,
    "Price" : None
}

def mean_tuple(x):
    sum = 0
    for i in x:
        sum += i
    mean = sum/len(x)
    return mean

with st.form(key = "ev_features"):

    st.subheader("Please input your desirable car features")

    form_values["Model Year"] = st.slider("Select which year's model do you prefer", 2011, 2024, 2023)

    form_values["Electric Vehicle Type"] = st.radio("Choose the type of Electric Vehicle", ['Battery Electric Vehicle (BEV)',
       'Plug-in Hybrid Electric Vehicle (PHEV)'], index = 0)
    
    ranges = st.slider("Select your desirable distance covered in one charge (in kms)", 20, 337, (100,200))
    form_values["Electric Range"] = mean_tuple(ranges)

    prices = st.slider("Select your price range (in dollars)", 27500, 71700, (30000,40000))
    form_values["Price"] = mean_tuple(prices)
    
    submit_button = st.form_submit_button(label = "Submit")

    if submit_button: 

        data = pd.DataFrame.from_dict([form_values])

        data_prepared = pipeline.transform(data)

        prediction = model.predict(data_prepared)

        st.write("The recommended Electric Vehicle for you is", prediction[0])



    