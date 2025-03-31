import streamlit as st

def app():
    

# Set the file path
    pdf_file_path = "template.pdf"  # Update the file path if needed

    # Read the PDF file as bytes
    with open(pdf_file_path, "rb") as file:
        pdf_bytes = file.read()

    # Create download section
    st.title("📥 Download Section")

    st.write("Click the button below to download the PDF file.")

    # Add download button
    st.download_button(
        label="📄 Download PDF",
        data=pdf_bytes,
        file_name="sample.pdf",
        mime="application/pdf"
    )

    