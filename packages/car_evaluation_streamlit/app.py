import requests

import streamlit as st

# Define the title 
st.title("Car evaluation web application")
st.write(
    "The model evaluates a cars acceptability based on the inputs below.\
    Pass the appropiate details about your car using the questions below to discover if your car is acceptable."
)

# Input 1
buying = st.radio(
    "What are your thought's on the cars buying price?",
    ("vhigh", "high", "med", "low")
)

# Input 2
maint = st.radio(
    "What are your thoughts on the price of maintanence for the car?",
    ("vhigh", "high", "med", "low")
)

# Input 3
doors = st.select_slider(
    "How many doors does the car have?",
    options=["2", "3", "4", "5more"]
)

# Input 4
persons = st.select_slider(
    "How many passengers can the car carry?",
    options=["2", "4", "more"]
)

# Input 5
lug_boot = st.select_slider(
    "What is the size of the luggage boot?",
    options=["small", "med", "big"]
)

# Input 6
safety = st.select_slider(
    "What estimated level of safety does the car provide?",
    options=["low", "med", "high"]
)

# Class values to be returned by the model 
class_values = {
    0: "unacceptable", 
    1: "acceptable", 
    2: "good", 
    3: "very good"
    }

# When 'Submit' is selected
if st.button("Submit"):

    # Inputs to ML model
    inputs = {
        "inputs": [
            {
                "buying": buying,
                "maint": maint, 
                "doors": doors, 
                "persons": persons,
                "lug_boot": lug_boot,
                "safety": safety
            }
        ]
        }
        
    # Posting inputs to ML API 
    response = requests.post(f"http://host.docker.internal:8001/api/v1/predict/", json=inputs, verify=False)
    json_response = response.json()

    prediction = class_values[json_response.get("predictions")[0]]

    st.subheader(f"This car is **{prediction}!**")


