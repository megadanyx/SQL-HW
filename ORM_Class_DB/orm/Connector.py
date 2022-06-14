import mysql.connector
def conn():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="e-shop"
    )
    return mydb
mydb = conn()