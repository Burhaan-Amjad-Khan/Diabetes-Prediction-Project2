# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("diabetes_model.pkl")

# Title
st.title("Diabetes Prediction Web App")

# Input fields
preg = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
glucose = st.number_input('Glucose Level', min_value=0, max_value=300, value=120)
bp = st.number_input('Blood Pressure', min_value=0, max_value=200, value=70)
skin = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)
insulin = st.number_input('Insulin', min_value=0, max_value=1000, value=79)
bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=25.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input('Age', min_value=1, max_value=120, value=33)

# Predict button
if st.button('Predict'):
    data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.error("The person is likely to have diabetes.")
    else:
        st.success("The person is not likely to have diabetes.")
