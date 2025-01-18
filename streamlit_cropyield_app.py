import streamlit as st
from fpdf import FPDF

# Function to generate a simple PDF report
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Test PDF Report", ln=True, align="C")
    pdf.cell(200, 10, txt="This is a sample PDF file created using Python.", ln=True, align="L")
    return pdf.output(dest="S").encode("latin1")

# Streamlit App
st.title("PDF Download Button Test")

# Button to generate and download PDF
if st.button("Generate PDF"):
    pdf_data = generate_pdf()
    st.download_button(
        label="📄 Download Report as PDF",
        data=pdf_data,
        file_name="test_report.pdf",
        mime="application/pdf"
    )
