# House_price_Estimator.py
import streamlit as st

st.set_page_config(page_title="City-Wise House Price Estimator", layout="centered")

st.title("🏙️ Location-Based House Price Estimator")
st.markdown("### 📊 Estimate Property Value Based on Location and Home Features")

# Location dropdown
location = st.selectbox("Select Location", ["Hyderabad", "Bangalore", "Mumbai"])

# User inputs
area = st.number_input("Enter Area (in sq ft)", min_value=300, max_value=10000, step=50)
bedrooms = st.slider("Number of Bedrooms", 1, 6, 2)
bathrooms = st.slider("Number of Bathrooms", 1, 6, 2)
floors = st.slider("Number of Floors", 1, 3, 1)
age = st.slider("Age of Property (Years)", 0, 50, 5)
parking = st.slider("Parking Spaces", 0, 3, 1)

# Set base price per sq ft for each city
price_map = {
    "Hyderabad": 5500,
    "Bangalore": 7500,
    "Mumbai": 12500
}

# Calculate price per sq ft adjustment
adjustment = 1.0
adjustment += (bedrooms - 2) * 0.02
adjustment += (bathrooms - 2) * 0.015
adjustment += (floors - 1) * 0.01
adjustment += (parking * 0.02)
adjustment -= (age * 0.005)  # older properties cheaper

# Calculate final price
base_rate = price_map[location]
final_rate = base_rate * adjustment
total_price = final_rate * area

if st.button("Estimate House Price"):
    st.markdown(f"""
    ### 🧾 Estimated Price:
    - **Price per sq ft:** ₹ {final_rate:,.2f}
    - **Total Price:** ₹ {total_price:,.2f}
    """)
