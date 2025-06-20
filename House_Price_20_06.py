import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🏠 House Price Prediction")
st.subheader("Enter the details below to predict the house price")

# User input
bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0.0, step=0.5)
living_area = st.number_input("Living Area (sqft)", min_value=0)
lot_area = st.number_input("Lot Area (sqft)", min_value=0)
floors = st.number_input("Number of Floors", min_value=0.0, step=0.5)
waterfront = st.selectbox("Waterfront Present", ["No", "Yes"])
views = st.number_input("Number of Views", min_value=0)
condition = st.slider("Condition of the House (1–5)", 1, 5)
grade = st.slider("Grade of the House (1–13)", 1, 13)
area_excl_basement = st.number_input("Area of the House (Excl. Basement)", min_value=0)
area_basement = st.number_input("Area of the Basement", min_value=0)
age = st.number_input("Age of the House (Years)", min_value=0)
living_area_renov = st.number_input("Living Area (After Renovation)", min_value=0)
lot_area_renov = st.number_input("Lot Area (After Renovation)", min_value=0)
schools_nearby = st.number_input("Number of Schools Nearby", min_value=0)
distance_airport = st.number_input("Distance from Airport (km)", min_value=0.0)

# Convert to binary
waterfront_binary = 1 if waterfront == "Yes" else 0

# Predict
if st.button("Predict House Price"):
    input_data = np.array([[bedrooms, bathrooms, living_area, lot_area, floors,
                            waterfront_binary, views, condition, grade,
                            area_excl_basement, area_basement, age,
                            living_area_renov, lot_area_renov,
                            schools_nearby, distance_airport]])
    
    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    st.success(f"🏡 Estimated House Price: ₹{prediction:,.2f}")
