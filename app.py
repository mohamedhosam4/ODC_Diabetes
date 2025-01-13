import streamlit as st
import pickle
import numpy as np
import requests
import os

# URL for direct download from GitHub
url = "https://raw.githubusercontent.com/mohamedhosam4/ODC_Diabetes/main/lr.pkl"

# Download the file from GitHub
response = requests.get(url)

# Save the downloaded file locally in the app
with open('lr.pkl', 'wb') as f:
    f.write(response.content)

# Load the model from the saved file
with open('lr.pkl', 'rb') as f:
    model = pickle.load(f)

# Display a success message once the model is loaded
st.write("Model loaded successfully!")

# App interface
st.title("Diabetes Prediction App")
st.header("Enter Patient Details:")

# Input fields for user data
pregnancies = st.number_input("Number of Pregnancies:", min_value=0, step=1)
glucose = st.number_input("Glucose Level:", min_value=0)
insulin = st.number_input("Insulin Level (IU/ml):", min_value=0)
bmi = st.number_input("Body Mass Index (BMI):", min_value=0.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function:", min_value=0.0, format="%.3f")
age = st.number_input("Age:", min_value=0, step=1)

# Button for making prediction
if st.button("Predict"):
    try:
        # Prepare the input data for prediction
        input_data = np.array([[pregnancies, glucose, insulin, bmi, dpf, age]])
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Display result based on prediction
        if prediction[0] == 1:
            st.error("The patient is likely to have diabetes.")
        else:
            st.success("The patient is not likely to have diabetes.")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Add footer (This page was created by Mohamed Hosam)
st.markdown(
    """
    <div style="position: fixed; bottom: 10px; left: 50%; transform: translateX(-50%); font-size: 14px; color: gray;">
        This page was created by <strong>Mohamed Hosam</strong>
    </div>
    """, unsafe_allow_html=True)
