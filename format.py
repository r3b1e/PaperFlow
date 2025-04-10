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
import pandas as pd
import json
import apsit_report


def create_connection():
    conn = database.create_connection()
    return conn


def generate_random():
        return random.randint(1000, 9999)
    
    
    # ----- for IEEE--------------------
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

# --------------------------for Apsit ---------------------------
def apsit_Paper(title_name='', leader_name='', member1='',member2='',member3='',guide_name='', abstract='', introduction='', methodology='', results='', conclusion='', reference=''):
    uid = st.session_state.uid
    st.session_state.generate = False

    st.header("or")
    ph = "Write Content"
    
    # Correctly placed and used
    title_name = st.text_input(" :orange[• Title Name of the Report]", title_name, placeholder="Enter full Report title")

    # Create 4 columns for names
    # Create 4 columns for member/leader names
    name_cols = st.columns(4)
    with name_cols[0]:
        member1 = st.text_input(
            " :orange[• Member 1 Name]",
            key="member1",
            placeholder="Enter Member 1 Name"
        )
    with name_cols[1]:
        member2 = st.text_input(
            " :orange[• Member 2 Name]",
            key="member2",
            placeholder="Enter Member 2 Name"
        )
    with name_cols[2]:
        member3 = st.text_input(
            " :orange[• Member 3 Name]",
            key="member3",
            placeholder="Enter Member 3 Name"
        )
    with name_cols[3]:
        leader_name = st.text_input(
            " :orange[• Leader Name]",
            key="leader",
            placeholder="Enter Leader Name"
        )

    # Create 4 columns for their Moodle IDs
    id_cols = st.columns(4)
    with id_cols[0]:
        id_1 = st.text_input(
            " :orange[• Member 1 ID]",
            key="id1",
            placeholder="Enter Moodle ID for Member 1"
        )
    with id_cols[1]:
        id_2 = st.text_input(
            " :orange[• Member 2 ID]",
            key="id2",
            placeholder="Enter Moodle ID for Member 2"
        )
    with id_cols[2]:
        id_3 = st.text_input(
            " :orange[• Member 3 ID]",
            key="id3",
            placeholder="Enter Moodle ID for Member 3"
        )
    with id_cols[3]:
        id_leader = st.text_input(
            " :orange[• Leader ID]",
            key="id_leader",
            placeholder="Enter Moodle ID for Leader"
        )



#======================================






#==========================================



    
        
    guide_name = st.text_input(" :orange[• Name of the Guide]", guide_name, placeholder="Enter guide")
    st.subheader("📄 Project Report Content")

    # st.subheader("📄 Project Report Content")

    abstract = st.text_area("📝 :orange[• Abstract]", placeholder="Write a summary of the project...", max_chars=1500)

    # 1. Introduction
    introduction = st.text_area("📘 :orange[1. Introduction]", placeholder="Provide a general introduction...", max_chars=1500)
    purpose = st.text_area("🎯 :orange[1.1 Purpose]", placeholder="State the purpose of the project...", max_chars=1000)
    problem_statement = st.text_area("❓ :orange[1.2 Problem Statement]", placeholder="Explain the problem addressed...", max_chars=1000)

    # For dynamic objectives and scope, use interactive version (shown earlier), but keeping static here:
    objectives = st.text_area("✅ :orange[1.3 Objectives]", placeholder="List the objectives...", max_chars=1000)
    scope = st.text_area("📌 :orange[1.4 Scope]", placeholder="Define the scope of the project...", max_chars=1000)

    # 2. Literature Review
    # Initialize session state to store entries and inputs


# Initialize session state

    st.subheader("📚 Add Literature Review Entry")

    # Input fields with placeholders
    title = st.text_input("📝 Title of Research Paper", placeholder="e.g. A Study on Machine Learning Algorithms")
    key_findings = st.text_area("🔍 Key Findings", placeholder="e.g. The paper concluded that Random Forest performs best on small datasets.")
    authors = st.text_input("👥 Author(s)", placeholder="e.g. John Doe, Jane Smith")
    year = st.text_input("📅 Publication Year", placeholder="e.g. 2024")

    # Initialize session state to store entries
    if "literature_data" not in st.session_state:
        st.session_state.literature_data = []

    # Add entry
    if st.button("➕ Add Entry"):
        if title and key_findings and authors and year:
            st.session_state.literature_data.append({
                "Sr. No": len(st.session_state.literature_data) + 1,
                "Title of Research Paper": title,
                "Key Findings": key_findings,
                "Author(s)": authors,
                "Publication Year": year
            })
            st.toast("✅ Entry added!")
        else:
            st.warning("⚠️ Please fill in all fields.")




    # 3. Proposed System
    proposed_system = st.text_area("💡 :orange[3. Proposed System]", placeholder="Describe your proposed solution...", max_chars=1500)
    features = st.text_area("⚙️ :orange[3.1 Features and Functionality]", placeholder="Mention key features and functionality...", max_chars=1000)

    # 4. Technical Specification
    technical_spec = st.text_area("🛠️ :orange[4. Technical Specification]", placeholder="List technical specifications, tools, and technologies...", max_chars=1500)

    # 5. Project Design
    st.subheader("🛠️ 5. Project Design")

    # Overall Design
    project_design = st.text_area(
        "Overall Design Summary",
        placeholder="E.g., Modular structure with layered architecture.",
        key="project_design"
    )

    # 5.1 Use Case Diagram
    st.markdown("### 👥 5.1 Use Case Diagram")
    use_case_heading = st.text_input(
        "Heading for Use Case Diagram",
        placeholder="E.g., Admin and User Functionalities",
        key="use_case_heading"
    )
    use_case_img = st.file_uploader("Upload Use Case Diagram Image", type=["png", "jpg", "jpeg"], key="use_case_img")
    
    if use_case_img:

        print(f"--------------------------hello{use_case_img} image url is ----------------------------------------")
        with open("use_case_img.png", "wb") as f:
            f.write(use_case_img.getbuffer())
        # st.markdown(f"#### {use_case_heading if use_case_heading else 'Use Case Diagram'}")
        # st.image(use_case_img, use_column_width=True)

    # 5.2 DFD (Data Flow Diagram)
    st.markdown("### 🔁 5.2 DFD (Data Flow Diagram)")
    dfd_heading = st.text_input(
        "Heading for DFD",
        placeholder="E.g., Level 0 - High-Level Data Flow",
        key="dfd_heading"
    )
    dfd_img = st.file_uploader("Upload DFD Image", type=["png", "jpg", "jpeg"], key="dfd_img")
    if dfd_img:
        with open("dfd_img.png", "wb") as f:
            f.write(dfd_img.getbuffer())
        # st.markdown(f"#### {dfd_heading if dfd_heading else 'Data Flow Diagram'}")
        # st.image(dfd_img, use_column_width=True)

    # 5.3 System Architecture
    st.markdown("### 🏗️ 5.3 System Architecture")
    architecture_heading = st.text_input(
        "Heading for System Architecture",
        placeholder="E.g., Client-Server Architecture with MySQL",
        key="architecture_heading"
    )
    architecture_img = st.file_uploader("Upload System Architecture Image", type=["png", "jpg", "jpeg"], key="architecture_img")
    if architecture_img:
        with open("architecture_img.png", "wb") as f:
            f.write(architecture_img.getbuffer())
        # st.markdown(f"#### {architecture_heading if architecture_heading else 'System Architecture'}")
        # st.image(architecture_img, use_column_width=True)

    implementation = st.text_area("🧩 :orange[5.4 Implementation]", placeholder="Explain implementation steps...", max_chars=1500)

    # 6. Project Scheduling
    scheduling = st.text_area("📅 :orange[6. Project Scheduling]", placeholder="Describe scheduling, timelines, and milestones...", max_chars=1000)

    # 7. Results
    results = st.text_area("📊 :orange[7. Results]", placeholder="Highlight the results achieved...", max_chars=1500)

    # 8. Conclusion
    conclusion = st.text_area("🔚 :orange[8. Conclusion]", placeholder="Conclude the project summary and insights...", max_chars=1000)

    # 9. Future Scope
    future_scope = st.text_area("🚀 :orange[9. Future Scope]", placeholder="Discuss how the project can be extended or improved...", max_chars=1000)

    # References
    reference = st.text_area("📖 :orange[• References]", placeholder="List your references or citations...", max_chars=1500)


    #collecting data from users
    data = {
        "title": title_name,
        "guide_name": guide_name,
        "members": json.dumps([
            {"name": member1, "id": id_1},
            {"name": member2, "id": id_2},
            {"name": member3, "id": id_3},
            {"name": leader_name, "id": id_leader}
        ]),
        "abstract": abstract,
        "introduction": introduction,
        "purpose": purpose,
        "problem_statement": problem_statement,
        "objectives": objectives,
        "scope": scope,
        "literature_review": json.dumps(st.session_state.literature_data),
        "proposed_system": proposed_system,
        "features": features,
        "technical_spec": technical_spec,
        "project_design": json.dumps({
            "Overall Design": project_design,
            "Use Case Diagram": use_case_heading,
            "DFD": dfd_heading,
            "Architecture": architecture_heading,
            "Implementation": implementation
        }),
        "scheduling": scheduling,
        "results": results,
        "conclusion": conclusion,
        "future_scope": future_scope,
        "references": reference
    }
    
    if st.button("Generate PDF"):
        st.session_state.generate = True
        
        
        
        # if st.session_state.get('randomid'):
        #     align_pdf.create_report(title, author, abstract, introduction, methodology, results, conclusion, reference)
        #     time.sleep(5)
        #     update_to_database(uid, st.session_state.randomid, title, author, abstract, introduction, methodology, results, conclusion, reference)
        # else:
        #     align_pdf.create_report(title, author, abstract, introduction, methodology, results, conclusion, reference)
        #     time.sleep(5)
        #     send_to_database(uid, title, author, abstract, introduction, methodology, results, conclusion, reference)

        # Set the file path
        apsit_report.apsit_formater(data)
        time.sleep(3)
        pdf_file_path = "apsit_project_report.pdf"  # Update the file path if needed

        # Read the PDF file as bytes
        with open(pdf_file_path, "rb") as file:
            pdf_bytes = file.read()

        # Create download section
        if st.session_state['generate']:
            
            
            st.title('See Prev')
            generated_pdf_path = "apsit_project_report.pdf" 
            
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


def fetch_records(user_id):
    conn = create_connection()
    if conn is None:
        return []  # Return an empty list if connection fails
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM paper WHERE uid = %s"
    cursor.execute(query, (user_id,))
    records = cursor.fetchall()
    conn.close()
    print(records)
    val = 1
    for i in records:
                paperInfo.app(i["title"], i["author"], i["uid"], val)
                val += 1    
    # return records


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
        choice = st.selectbox('New Paper / Previous Paper', ['Create a new Paper', 'My previous Records', 'APSIT Report Format'])

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
            
            fetch_records(2)
# ----------------------apsit format ----------------------------------
        if choice == 'APSIT Report Format':
            st.title("🎓 APSIT Report Format")
            # Define the path to your PDF file
            pdf_path = "24-25__Even_Mini project-1B report format_first 5 Pages (1).pdf" 
            
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
                apsit_Paper()
            
            
            
        
        
        
        
    else:
        st.error("Login User Can Only Format")
        
    
    

