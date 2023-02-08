import mysql.connector
from mysql.connector import Error
import pandas as pd

def initialize_database():
    # Verbindung mit Datenbank
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    my_cursor = my_db.cursor()

    # Wenn es noch keine Datenbank mit dem Namen "notenuebersicht" gibt wird eine erstellt
    my_cursor.execute("SHOW DATABASES LIKE 'notenuebersicht'")
    result = my_cursor.fetchall()
    x = []
    if result == x:
        my_cursor.execute("CREATE DATABASE notenuebersicht")

def erstelle_tabelle(name):
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="notenuebersicht",
        password="password"
    )
    my_cursor = my_db.cursor()
    test = f"SHOW TABLES LIKE '{name}'"
    my_cursor.execute(test)
    result = my_cursor.fetchone()
    if result:
        x = 0;
    else:
        sql = f"""
                    CREATE TABLE `{name}`(
                        mtknr VARCHAR(255) DEFAULT NULL,
                        sortname VARCHAR(255) NULL,
                        bewertung VARCHAR(255) NULL,
                        pstatus VARCHAR(255) NULL,
                        pversuch VARCHAR(255) NULL,
                        ktxt VARCHAR(255) NULL,
                        spversion VARCHAR(255) NULL,
                        semester VARCHAR(255) NULL,
                        pdatum VARCHAR(255) NULL,
                        pnr VARCHAR(255) NULL,
                        bonus VARCHAR(255) NULL,
                        labnr VARCHAR(255) NULL,
                        pordnr VARCHAR(255) NULL,
                        porgnr VARCHAR(255) NULL,
                        mail VARCHAR(255) NULL,
                        fach VARCHAR(255) NULL,
                        `Dozierende Person` VARCHAR(255) NULL
                        )
                """
        my_cursor.execute(sql)

def loesche_tabelle(name):
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="notenuebersicht",
        password="password"
    )
    my_cursor = my_db.cursor()
    test = f"SHOW TABLES LIKE '{name}'"
    my_cursor.execute(test)
    result = my_cursor.fetchone()
    if result:
        my_cursor.execute(f"DROP TABLE {name}")

def einlesen(fach, doz):
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="notenuebersicht",
        password="password"
    )
    my_cursor = my_db.cursor()

    spalten = ['mtknr','sortname','bewertung','pstatus','pversuch','ktxt','spversion','semester','pdatum','pnr','bonus','labnr','pordnr','porgnr','mail','fach','`Dozierende Person`']
    text = ''

    for i in range(0, 17):
        text += spalten[i]
        if (i == 16):
            break
        text += ', '

    df = pd.read_csv("CSV/csv_sorted.csv", index_col=False, delimiter=',')

    for i, row in df.iterrows():
        # sql = f"INSERT INTO Tabelle VALUES ({spalten}) ({'%s,' * 15}%s,%s)"
        # my_cursor.execute(sql, tuple(row) + (fach, doz))
        # sql = f"INSERT INTO Tabelle ({text}) VALUES ({spalten}) (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"#,'{fach}','{doz}')"
        # my_cursor.execute(sql, tuple(row))
        sql = f"INSERT INTO Tabelle ({text}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        my_cursor.execute(sql, tuple(row) + (fach, doz))
        my_db.commit()

    # my_cursor.execute(sql)
    # my_db.commit()

def suche(suchbegriff):
    # Verbindung zur Datenbank herstellen
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="notenuebersicht",
        password="password"
    )
    my_cursor = my_db.cursor()

    # Abfrage erstellen und ausführen
    query = "SELECT * FROM Tabelle WHERE sortname LIKE '%{}%'".format(suchbegriff)
    my_cursor.execute(query)

    # Ergebnisse auslesen
    result = my_cursor.fetchall()

    # Verbindung zur Datenbank schließen
    my_db.close()

    # Ergebnisse ausgeben
    for i in result:
        print(i)

