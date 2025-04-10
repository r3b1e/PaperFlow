
import streamlit as st
import base64
import os
import tempfile
def app():

 
    st.title("📄 APSIT Project Report Preview")

    # Option 1: Use a file uploader instead of a hard-coded path
    st.subheader("Upload your PDF")
    uploaded_file = st.file_uploader("Choose your PDF file", type="pdf")

    if uploaded_file is not None:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            # Write the uploaded content to the temp file
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        # Display PDF using PDF.js viewer (more robust for large files)
        st.markdown(f"""
            <iframe
                src="https://mozilla.github.io/pdf.js/web/viewer.html?file=data:application/pdf;base64,{base64.b64encode(uploaded_file.getvalue()).decode('utf-8')}"
                width="700"
                height="800"
                style="border: none;"
            ></iframe>
        """, unsafe_allow_html=True)
        
        # Add download button
        st.download_button(
            label="📥 Download PDF",
            data=uploaded_file.getvalue(),
            file_name=uploaded_file.name,
            mime="application/pdf"
        )
        
        # Clean up the temporary file
        os.unlink(tmp_file_path)

    # Option 2: Alternative approach using hard-coded path
    st.subheader("Or use pre-loaded PDF")

    if st.button("Click to Preview & Download Report"):
        pdf_path = "apsit_project_report.pdf"  # Make sure this file is in the same directory
        
        try:
            with open(pdf_path, "rb") as f:
                pdf_data = f.read()
                
                # Display a smaller preview instead of the full document
                st.warning("Showing preview. Large PDFs may not render completely in the preview.")
                
                # Create a preview with limited height to improve performance
                pdf_preview = f'<iframe src="data:application/pdf;base64,{base64.b64encode(pdf_data).decode("utf-8")}" width="700" height="500" type="application/pdf"></iframe>'
                st.markdown(pdf_preview, unsafe_allow_html=True)
                
                # Add download button
                st.download_button(
                    label="📥 Download Full PDF",
                    data=pdf_data,
                    file_name="apsit_project_report.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.error(f"❌ PDF file not found: {pdf_path}")
            st.info("Please make sure the PDF file is in the same directory as your Streamlit app.")

    # Add helpful instructions
    st.markdown("### Troubleshooting")
    st.markdown("""
    - If the PDF doesn't display correctly, try using the download button to view it locally
    - For very large PDFs (>2MB), the preview may be limited, but download should work properly
    - Make sure the PDF file is in the correct location if using Option 2
    """)