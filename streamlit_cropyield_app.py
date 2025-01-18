import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time  # For loading animation
from fpdf import FPDF  # Library for PDF generation

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

# Function to generate a PDF report
def generate_pdf_report(crop_type, planting_area, soil_condition, fertilizer, pesticide, water_avail, yield_estimate):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Crop Yield Estimation Report", ln=True, align="C")
    pdf.ln(10)

    # Add content
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Crop Type: {crop_type}", ln=True)
    pdf.cell(200, 10, txt=f"Planting Area: {planting_area:.2f} hectares", ln=True)
    pdf.cell(200, 10, txt=f"Soil Condition: {soil_condition}", ln=True)
    pdf.cell(200, 10, txt=f"Fertilizer Usage: {fertilizer:.2f} kg/ha", ln=True)
    pdf.cell(200, 10, txt=f"Pesticide Usage: {pesticide:.2f} L/ha", ln=True)
    pdf.cell(200, 10, txt=f"Water Availability: {water_avail:.2f} mm", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Estimated Yield: {yield_estimate:.2f} tons", ln=True)

    # Save PDF as a binary file in memory
    return pdf.output(dest="S").encode("latin1")

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
st.title("🌾 Crop Yield Estimation Web App")

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

    # Generate and download PDF report
    pdf_data = generate_pdf_report(crop_type, planting_area, soil_condition, fertilizer, pesticide, water_avail, yield_estimate)
    st.download_button(
        label="📄 Download Report as PDF",
        data=pdf_data,
        file_name="crop_yield_report.pdf",
        mime="application/pdf"
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ using Streamlit")
