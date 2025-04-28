import streamlit as st
import format

# Define the function to run when the button is clicked


# Define custom CSS to create a div with text and button
def app(title, author, uid, i, paperContent):
    
    
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
            f"""
            <div class="custom-container">
                <div class="text-content">
                    <h6>Title : {title}</h6>
                    <h6>Author : {author}</h6>
                    <h6>Date : 25-05-25</h6>
                </div>
                <div class="button-container">
                    <!-- Button placeholder -->
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Use st.button() to trigger a Python function with a unique key
        # col1, col2, col3 = st.columns([4, 1, 1])  # Column layout to align button to the right
        # # col = st.columns([1])
        # with col1:
        # if st.button("Click Me", key=i):  # Add a unique key
                
        #     print(paperContent)
        #     format.my_function(paperContent)
            
        if st.button("Click Me", key=i):
    # Set the page to Create a new Paper
             # Store the clicked paper's data
            print('happy')
            st.session_state.selected_paper_data = paperContent
            st.session_state.choice = 'Create a new Paper'

   
            
            
            
            
