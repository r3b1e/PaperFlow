import streamlit as st

# Define the function to run when the button is clicked
def my_function():
    st.success("✅ Button clicked! The function has been executed successfully.")

# Define custom CSS to create a div with text and button

def app():
    st.markdown(
        """
        <style>
        .custom-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #f0f2f6;
            padding: 10px 20px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
        }
        .text-content {
            font-size: 16px;
            color: #333;
        }
        .text-content h6 {
            margin: 0;
            padding: 0;
        }
        .button-container {
            display: flex;
            align-items: center;
        }
        .button-container button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .button-container button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create a container for dynamic content
    with st.container():
        # Create div with text and button using markdown
        st.markdown(
            """
            <div class="custom-container">
                <div class="text-content">
                    <h6>Title : Jorg Divine</h6>
                    <h6>Author : Andrew Nafak</h6>
                    <h6>Date : 25-05-25</h6>
                </div>
                <div class="button-container">
                    <!-- Button placeholder -->
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Use st.button() to trigger a Python function
        col1, col2, col3 = st.columns([4, 1, 1])  # Column layout to align button to the right
        with col3:
            if st.button("Click Me"):
                my_function()
