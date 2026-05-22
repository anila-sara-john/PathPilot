import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",           # your MySQL host
        user="root",                # MySQL username
        #password="YOUR_MYSQL_PASSWORD",         # MySQL password you set    # CHANGE THIS LOCALLY IN YOUR COMPUTER
        password="root123",
        database="pathpilot_db"     # name of your database
    )
