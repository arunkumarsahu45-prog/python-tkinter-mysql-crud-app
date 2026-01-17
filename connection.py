import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="Arun@123")

if conn.is_connected():
    print("Successfully connected to the database") 
print(conn)
print(conn.is_connected())