# Import Libraries

import streamlit as st
import numpy as np
import pickle

# Load Model

model = pickle.load(open("diabetes_model.pkl", "rb"))

# Load Scaler

scaler = pickle.load(open("scaler.pkl", "rb"))

# App Title

st.title("Diabetes Prediction System")

st.write(
    "Enter patient medical details to predict diabetes risk."
)

# User Inputs

pregnancies = st.number_input("Pregnancies", min_value=0)

glucose = st.number_input("Glucose")

blood_pressure = st.number_input("Blood Pressure")

skin_thickness = st.number_input("Skin Thickness")

insulin = st.number_input("Insulin")

bmi = st.number_input("BMI")

dpf = st.number_input("Diabetes Pedigree Function")

age = st.number_input("Age")

# Prediction Button

if st.button("Predict"):

    # Input Data

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    # Scale Input

    input_scaled = scaler.transform(input_data)

    # Prediction

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]

    # Display Result

    if prediction == 1:
        
        st.error(
            f"High Diabetes Risk Detected "
            f"(Probability: {probability:.2f})"
        )

    else:
        
        st.success(
            f"Low Diabetes Risk "
            f"(Probability: {probability:.2f})"
        )