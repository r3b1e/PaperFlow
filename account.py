import streamlit as st
import mysql.connector
import database


def create_connection():
    conn = database.create_connection()
    return conn

# def add_user(username, password):
#     try:
#         mydb = create_connection()
#         mycursor = mydb.cursor()
#         sql = "insert into user_info(username, password) values(%s, %s)"
#         val = (username, password)
#         mycursor.execute(sql, val)
#         mydb.commit()
#         mydb.close()
#     except:
#         st.warning('Login Failed')
    
# def authentication_user(email, password):
#     mydb = create_connection()
#     mycursor = mydb.cursor()
#     sql = "select * from user_info where email = %s and password = %s"
#     val = (email, password) 
#     mycursor.execute(sql, val)
#     user = mycursor.fetchone()
#     print(user)
#     print(type(user))
#     mydb.close()
#     return user




def app():
    
    st.title("Welcome to :violet[PaperFlow] :sunglasses:")
     
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'uid' not in st.session_state:
        st.session_state.uid = ''
        
    # authentication_user("sunny", "sunny@98")
    def authentication_user(email, password):
        try:
            mydb = create_connection()
            mycursor = mydb.cursor()
            sql = "SELECT * FROM user_info WHERE email = %s AND password = %s"
            val = (email, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()
            
            if user is None:
                raise ValueError("Invalid login credentials")

            print(user)
            print(type(user))
            user_id = user[0]
            username = user[1]
            user_email = user[2]
    
            st.session_state.username = username
            st.session_state.useremail = user_email
            st.session_state.uid = user_id
            st.session_state.signedout = True
            st.success('Login Sucessfully Successfully!')
            
            # st.write("sucessfull")
            
        except ValueError as e:
            st.warning(str(e))  # Show a custom error message
        except Exception as e:
            st.warning('An unexpected error occurred')
            
            
    def add_user(username,email, password):
        try:
            mydb = create_connection()
            mycursor = mydb.cursor()
            sql = "insert into user_info(username, email, password) values(%s, %s, %s)"
            val = (username, email, password)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
        except:
            st.warning('Login Failed')
    
    def t():
        st.session_state.signedout = False
        # st.session_state.signout = False
        st.session_state.username = ""
        st.session_state.useremail = ""

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
        
    if not st.session_state['signedout']:
        st.header("🔐 :violet[Login & Signup] System")
        choice = st.selectbox('Login/Singup', ['LogIn', 'SignUp'])
        if choice == 'LogIn':
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            st.button("LogIn", on_click=authentication_user(email, password))
        else:
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            username = st.text_input('Unique UserName')
            if st.button("Create My Account"):
                if email and password and username:
                    add_user(username, email, password)
                    st.success('Account created Successfully!')
                    st.markdown('Please Login using your email and password')
            else:
                st.error("Please fill in all fields.")
            
    if st.session_state['signedout']:
        
        st.text('Name: ' + st.session_state.username)
        st.text('Email: ' + st.session_state.useremail)
        st.button('Sing Out', on_click=t)

    
    
    
    
        
    

    