import streamlit as st
import requests

# ---------------------------------------------------------
# [CONFIG] Paste your Render API URL here (no trailing slash)
# ---------------------------------------------------------
API_URL = "https://iris-classifier-pipeline.onrender.com" 
# ---------------------------------------------------------

st.title("🌸 Iris Flower Predictor")
st.write("Enter the flower's measurements below to predict its species.")

# 1. Create Input Sliders for the 4 Features
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# 2. The "Predict" Button
if st.button("🔍 Identify Flower"):
    # payload is the data we send to the API
    payload = {
        "features": [sepal_length, sepal_width, petal_length, petal_width]
    }
    
    try:
        # Send the data to your Cloud API
        st.info(f"Connecting to Cloud Brain at: {API_URL}...")
        response = requests.post(f"{API_URL}/predict", json=payload)
        
        # Get the answer
        result = response.json()
        
        # Display the Result cleanly
        st.success(f"🌺 Prediction: **{result['class']}**")
        st.write(f"Model Output ID: {result['prediction']}")
        
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
