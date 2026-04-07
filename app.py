import streamlit as st
import pandas as pd
import requests
import os

st.set_page_config(page_title="Healthcare Diagnosis Assistant", layout="centered")
st.title("🩺 Healthcare Diagnosis Assistant")
st.write("Select your symptoms below (1 = Yes, 0 = No)")

# 1️⃣ Load dataset columns dynamically
dataset_path = os.path.join("..", "ml-pipeline", "data", "dataset.csv")
df = pd.read_csv(dataset_path)

# All columns except target 'prognosis'
symptoms = [col for col in df.columns if col != "prognosis"]

# 2️⃣ Create radio buttons dynamically
user_input = {}
for symptom in symptoms:
    user_input[symptom] = st.radio(symptom, [0, 1], index=0)

# 3️⃣ Predict button
if st.button("Predict Disease"):
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=user_input)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Disease: {result['predicted_disease']}")
        else:
            st.error(f"Error: {response.json()}")
    except Exception as e:
        st.error(f"Server not running or error: {str(e)}")