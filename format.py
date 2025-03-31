import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader
import base64
import paperInfo
import random
import mysql.connector
import database
import extract
import align_pdf
import time

def create_connection():
    conn = database.create_connection()
    return conn


def generate_random():
        return random.randint(1000, 9999)
    
def papers(title = '', author = '', abstract='', introduction='', methodology='', results='', conclusion='', reference=''):
            
        uid = st.session_state.uid
        
        
        st.session_state.generate = False
            
            
        st.header("or")
        ph="Write Content"
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input(" :orange[• Title of the Paper]",title.capitalize(), placeholder="Enter title")
        with col2:
            author = st.text_input(" :orange[• Author Name]",author.capitalize(), placeholder="Enter author")
        abstract=st.text_area(label=' :orange[• Abstract]',value=abstract, placeholder=ph,height=None, max_chars=1000)
        introduction=st.text_area(label=' :orange[1 Introduction]',value=introduction,placeholder=ph,height=None, max_chars=1000)
        methodology=st.text_area(label=' :orange[2 Methodogy]',value=methodology,placeholder=ph,height=None, max_chars=1000)
        results=st.text_area(label=' :orange[3 Result]',value=results,placeholder=ph,height=None, max_chars=1000)
        conclusion=st.text_area(label=' :orange[4 Conclusion]',value=conclusion,placeholder=ph,height=None, max_chars=1000)
        reference=st.text_area(label=' :orange[• reference]',value=reference,placeholder=ph,height=None, max_chars=1000)
            
        if st.button("Generate PDF"):  # Add a unique key
            st.session_state.generate = True
            if st.session_state['randomid']:
                align_pdf.create_report(title, author, abstract, introduction, methodology, results, conclusion, reference)
                update_to_database(uid,st.session_state.randomid, title, author, abstract, introduction, methodology, results, conclusion, reference)
            else:  
                send_to_database(uid, title, author, abstract, introduction, methodology, results, conclusion, reference)

        # Set the file path
        pdf_file_path = "combined_project_report.pdf"  # Update the file path if needed

        # Read the PDF file as bytes
        with open(pdf_file_path, "rb") as file:
            pdf_bytes = file.read()

        # Create download section
        if st.session_state['generate']:
            time.sleep(5)
            
            st.title('See Prev')
            generated_pdf_path = "combined_project_report.pdf" 
            
            def generated_pdf():
                # st.session_state.generated_prev = not st.session_state.generated_prev
                print("generated_pdf")

            
            if 'generated_prev' not in st.session_state:
                st.session_state.generated_prev = False
                
            st.subheader("PDF Preview:")
            st.button("Preview", on_click=generated_pdf)
            # Make sure the file exists in the same directory or provide the correct path
            if not st.session_state['generated_prev']:
                

                try:
                    # Open and read the PDF file in binary mode
                    
                    with open(generated_pdf_path, "rb") as f:
                        pdf_bytes = f.read()

                    # Encode the PDF to base64
                    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

                    # Create an iframe to display the PDF
                    pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500"></iframe>'
                    
                    st.markdown(pdf_display, unsafe_allow_html=True)

                except FileNotFoundError:
                    st.error(f"File not found at: {generated_pdf_path}")
            st.markdown("<br><br>", unsafe_allow_html=True) 
            
            
            st.title("📥 Download Section")

            st.write("Click the button below to download the PDF file.")

            # Add download button
            st.download_button(
                label="📄 Download PDF",
                data=pdf_bytes,
                file_name="sample.pdf",
                mime="application/pdf"
        )

        
        
def update_to_database(uid, paperid, title, author, abstract, introduction, methodology, results, conclusion, reference):
    try:
        mydb = create_connection()
        mycursor = mydb.cursor()

        sql = '''
        UPDATE paper
        SET title = %s, 
            author = %s, 
            abstract = %s, 
            introduction = %s, 
            methodology = %s, 
            results = %s, 
            conclusion = %s, 
            refer = %s
        WHERE paperid = %s AND uid = %s
        '''
        val = (title, author, abstract, introduction, methodology, results, conclusion, reference, paperid, uid)

        mycursor.execute(sql, val)
        mydb.commit()

        st.success('Updates are made successfully!')
    
    except Exception as e:
        st.error('Failed to commit while updating')
        print(f"Failed to commit: {e}")
    
    finally:
        # Close cursor and database connection
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

       

def send_to_database(uid, title, author, abstract, introduction, methodology, results, conclusion, reference):
    try:
        paperid = generate_random()
        print(paperid)
        print(uid)

        mydb = create_connection()
        mycursor = mydb.cursor()

        sql = 'INSERT INTO paper (uid, paperid, title, author, abstract, introduction, methodology, results, conclusion, refer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (uid, paperid, title, author, abstract, introduction, methodology, results, conclusion, reference)
        # val = (7, 7, "something", "something", "something", "something", "something", "something", "something", "something")

        print('not executing')
        mycursor.execute(sql, val)
        print('executing successfully')

        mydb.commit()
        
        # Store the generated paperid in session state
        st.session_state.randomid = paperid
        st.success('Changes are made successfully!')
    
    except Exception as e:
        print(f"Failed to commit: {e}")
        st.error('Failed to commit while creating')
    
    finally:
        # Ensure the connection is closed properly
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

        

def app():
    
    
    if 'randomid' not in st.session_state:
        st.session_state.randomid = 0
        
    if 'isData' not in st.session_state:
        st.session_state.isData = False
        
    if 'generate' not in st.session_state:
        st.session_state.generate = True
        
    username = st.session_state.username.capitalize()
    
    
    
    if not username == "":
        st.header(f":violet[{username}]") 
        choice = st.selectbox('New Paper / Previous Paper', ['Create a new Paper', 'My previous Records'])

        if choice == 'Create a new Paper':
            st.title("IEEE Format PDF Viewer")
            # Define the path to your PDF file
            pdf_path = "template.pdf" 
            
            def reverse():
                st.session_state.prev = not st.session_state.prev

            
            if 'prev' not in st.session_state:
                st.session_state.prev = False
                
            st.subheader("PDF Preview:")
            st.button("See Preview  1", on_click=reverse)
            # Make sure the file exists in the same directory or provide the correct path
            if st.session_state['prev']:
                

                try:
                    # Open and read the PDF file in binary mode
                    
                    with open(pdf_path, "rb") as f:
                        pdf_bytes = f.read()

                    # Encode the PDF to base64
                    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

                    # Create an iframe to display the PDF
                    pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500"></iframe>'
                    
                    st.markdown(pdf_display, unsafe_allow_html=True)

                except FileNotFoundError:
                    st.error(f"File not found at: {pdf_path}")
            st.markdown("<br><br>", unsafe_allow_html=True) 
                    
            uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
            
            if uploaded_file is not None:
                st.session_state.isData = True
                extract.pdf_send(uploaded_file)
                
            if uploaded_file is None:
                st.session_state.isData = False
            
            if not st.session_state["isData"]:
                papers()
            
            
        if choice == 'My previous Records':
            for i in range(0, 5):
                paperInfo.app(i)
            
        
        
        
        
    else:
        st.error("Login User Can Only Format")
        
    
    

