import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
with open('final_model.joblib', 'rb') as file:
    model = joblib.load(file)

# Prediction function
def prediction(inp_list):
    pred = model.predict([inp_list])[0]
    if pred == 0:
        return "Sitting on bed"
    elif pred == 1:
        return 'Sitting on chair'
    elif pred == 2:
        return 'Lying on bed'
    else:
        return "Ambulating"

# Streamlit App
def main():
    st.title("📡 ACTIVITY PREDICTION FROM SENSOR DATA")
    st.subheader(
        "This application predicts the ongoing activity based on sensor data. "
        "Fill in the values and click *Predict* to see the result."
    )

    st.image('imagedep.jpg', caption="Sensor Setup")

    # RFID Config
    rfid = st.selectbox("Select RFID Configuration", ['Config 1 (4 Sensors)', 'Config 2 (3 Sensors)'])
    st.image('rfidimg.jpg', caption="RFID Config Illustration")

    # Fix lambda logic (space in config name was wrong)
    rfid_e = 3 if '3 Sensors' in rfid else 4

    # User inputs
    ant_ID = st.selectbox('Select the Antenna ID', [1, 2, 3, 4])
    rssi = st.text_input('Enter RSSI (Received Signal Strength Indicator)')
    accv = st.text_input('Enter Vertical Acceleration')
    accf = st.text_input('Enter Frontal Acceleration')
    accl = st.text_input('Enter Lateral Acceleration')

    # Prediction
    if st.button('Predict'):
        try:
            inp_data = [float(accf), float(accv), float(accl), int(ant_ID), float(rssi), int(rfid_e)]
            response = prediction(inp_data)
            st.success(f"Predicted Activity: **{response}**")
        except ValueError:
            st.error("Please ensure all fields are filled with **valid numeric values**.")

# Run app
if __name__ == '__main__':
    main()

