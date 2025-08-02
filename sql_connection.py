import mysql.connector
def connect():
    db=mysql.connector.connect(
        host="192.168.178.167",
        user="lordrasgath",
        password="januar",
        database="airbnb_test"
    )
    return db

