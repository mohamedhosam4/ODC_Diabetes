import streamlit as st
import pickle
import numpy as np
import requests

url = "https://drive.google.com/uc?id=1Oqav3S8ROiZdNHMUCe7Bg-rOGuSNhwQP"
output = "lr.pkl"

try:
    response = requests.get(url, allow_redirects=True)
    with open(output, "wb") as file:
        file.write(response.content)
except Exception as e:
    st.error(f"Error downloading the model using requests: {e}")


st.title("Diabetes Prediction App")
st.header("Enter Patient Details:")

pregnancies = st.number_input("Number of Pregnancies:", min_value=0, step=1)
glucose = st.number_input("Glucose Level:", min_value=0)
insulin = st.number_input("Insulin Level (IU/ml):", min_value=0)
bmi = st.number_input("Body Mass Index (BMI):", min_value=0.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function:", min_value=0.0, format="%.3f")
age = st.number_input("Age:", min_value=0, step=1)

if st.button("Predict"):
    try:
        input_data = np.array([[pregnancies, glucose, insulin, bmi, dpf, age]])
        prediction = model.predict(input_data)
        
        if prediction[0] == 1:
            st.error("The patient is likely to have diabetes.")
        else:
            st.success("The patient is not likely to have diabetes.")
    except Exception as e:
        st.error(f"Error during prediction: {e}")


st.markdown(
    """
    <div style="position: fixed; bottom: 10px; left: 50%; transform: translateX(-50%); font-size: 14px; color: gray;">
        This page was created by <strong>Mohamed Hosam</strong>
    </div>
    """, unsafe_allow_html=True)
