import mysql.connector
def connect():
    db=mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    return db

