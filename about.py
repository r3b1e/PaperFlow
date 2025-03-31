import streamlit as st

def app():

    st.title("Upload a PDF")

    # Create two input fields for Title and Author
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Title", placeholder="Enter title")
    with col2:
        author = st.text_input("Author", placeholder="Enter author")

    # Space and buttons aligned to the right
    col3, col4, col5 = st.columns([5, 1, 1])
    with col4:
        add_button = st.button("Add")
    with col5:
        clear_button = st.button("Clear")

    # Handle button actions
    if add_button:
        st.success(f"Added: {title} by {author}")
    if clear_button:
        st.warning("Cleared the fields")

    # Optional PDF file upload
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        