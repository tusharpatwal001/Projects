import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below: ")


# input fields
age = st.number_input("Age", min_value=1, max_value=119, value=22)
weight = st.number_input("Weight (Kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5,
                         max_value=2.5,  value=1.78)
income_lpa = st.number_input(
    "Annual Income (LPA)", min_value=0.1, max_value=10.0, value=2.6)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Delhi").capitalize()
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job',
        'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        'age': age,
        'weight': weight,
        'height': height,
        'income_lpa': income_lpa,
        'smoker': smoker,
        'city': city,
        'occupation': occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            if result['predicted_category'] == "High":
                st.warning(
                    f"Predict Insurance Premium Category: **{result['predicted_category']}**")
            elif result['predicted_category'] == "Medium":
                st.info(
                    f"Predict Insurance Premium Category: **{result['predicted_category']}**")
            else:
                st.success(
                    f"Predict Insurance Premium Category: **{result['predicted_category']}**")

        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the FastAPI server. Make sure it's running on port 8000.")
