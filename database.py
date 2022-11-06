import mysql.connector


def initialize_database():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    my_cursor = my_db.cursor()
    my_cursor.execute("SHOW DATABASES LIKE 'notenuebersicht'")
    result = my_cursor.fetchall()

    x = []

    if result == x:
        my_cursor.execute("CREATE DATABASE notenuebersicht")
