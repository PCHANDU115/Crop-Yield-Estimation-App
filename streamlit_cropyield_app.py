import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time  # For loading animation

# Define the crop yield estimation function
def estimate_yield(crop_type, planting_area, soil_condition, fertilizer, pesticide, water_avail):
    crop_coefficients = {'Wheat': 1.2, 'Corn': 1.5, 'Rice': 1.3}
    soil_coefficients = {'Good': 1.1, 'Average': 1.0, 'Poor': 0.9}

    crop_coeff = crop_coefficients.get(crop_type, 1.0)
    soil_coeff = soil_coefficients.get(soil_condition, 1.0)

    # Calculate the yield estimate considering fertilizers, pesticide, and water
    yield_estimate = crop_coeff * soil_coeff * planting_area + (fertilizer * 0.01) + (pesticide * 0.5) + (water_avail * 0.2)
    return yield_estimate

# Function to plot the Pie Chart
def plot_yield_pie(crop_type, fertilizer, pesticide, water_avail):
    labels = ['Fertilizer', 'Pesticide', 'Water Availability']
    sizes = [fertilizer, pesticide, water_avail]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99', '#ff6666'])
    ax.set_title(f"Contributions to {crop_type} Yield")
    st.pyplot(fig)

# Set the theme
st.sidebar.title("⚙️ App Settings")
theme = st.sidebar.radio("Choose a Theme:", ["🌞 Light", "🌙 Dark"], index=0)
if theme == "🌞 Light":
    st.markdown(
        """
        <style>
        body {background-color: #f9f9f9; color: #333;}
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        body {background-color: #333; color: #f9f9f9;}
        </style>
        """,
        unsafe_allow_html=True,
    )

# App Title with Emoji
st.title("🌾 Crop Yield Estimation Web app")

# Input Section
st.header("📋 Input Parameters")
crop_type = st.selectbox("🌾 Select Crop Type:", ['Wheat', 'Corn', 'Rice'])
planting_area = st.number_input("🧑‍🌾 Enter Planting Area (hectares):", min_value=0.0, step=0.1)
soil_condition = st.selectbox("🪴 Select Soil Condition:", ['Good', 'Average', 'Poor'])
fertilizer = st.number_input("🌱 Enter Fertilizer Usage (kg/ha):", min_value=0.0, step=0.1)
pesticide = st.number_input("🛡️ Enter Pesticide Usage (L/ha):", min_value=0.0, step=0.1)
water_avail = st.number_input("💧 Enter Water Availability (mm):", min_value=0.0, step=0.1)

# Estimate Button with Loading Animation
if st.button("📊 Estimate Yield"):
    with st.spinner("Calculating... Please wait 🕒"):
        time.sleep(2)  # Simulate processing time
        yield_estimate = estimate_yield(crop_type, planting_area, soil_condition, fertilizer, pesticide, water_avail)
        st.success(f"✅ Estimated Crop Yield: {yield_estimate:.2f} tons")

    # Display Pie Chart
    st.subheader("📈 Yield Contributions")
    plot_yield_pie(crop_type, fertilizer, pesticide, water_avail)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ using Streamlit")
