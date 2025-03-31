# Hash password
import mysql.connector
import hashlib
import security_pass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create MySQL connection

# conn == mydb
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Change this
        password=security_pass.pass_key,  # Change this
        database="PAPER_FLOW"
    )
    return conn

mycursor = create_connection().cursor()
print("mycursor")