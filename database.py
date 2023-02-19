import mysql.connector
import pandas as pd

def initialize_database():
    # connecting to databse
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    my_cursor = mydb.cursor()

    # if there is no database with the name "notenuebersicht", create one
    my_cursor.execute("SHOW DATABASES LIKE 'notenuebersicht'")
    result = my_cursor.fetchall()
    x = []
    if result == x:
        my_cursor.execute("CREATE DATABASE notenuebersicht")

def erstelle_tabelle(name):
    # connecting to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="notenuebersicht",
        password="password"
    )
    my_cursor = mydb.cursor()
    test = f"SHOW TABLES LIKE '{name}'"
    my_cursor.execute(test)
    result = my_cursor.fetchone()

    # If there is no table with given name, create one
    if result:
        return
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
                        `Dozierende Person` VARCHAR(255) NULL,
                        PRIMARY KEY (mtknr, pdatum)
                        )
                """
        my_cursor.execute(sql)

def loesche_tabelle(name):
    # connecting to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="notenuebersicht",
        password="password"
    )
    my_cursor = mydb.cursor()
    test = f"SHOW TABLES LIKE '{name}'"
    my_cursor.execute(test)
    result = my_cursor.fetchone()

    # column with given name is deleted
    if result:
        my_cursor.execute(f"DROP TABLE {name}")

def einlesen(fach, doz):
    # connecting to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="notenuebersicht",
        password="password"
    )
    my_cursor = mydb.cursor()

    spalten = ['mtknr','sortname','bewertung','pstatus','pversuch','ktxt','spversion','semester','pdatum','pnr','bonus','labnr','pordnr','porgnr','mail','fach','`Dozierende Person`']
    text = ''

    # creating string with the names
    for i in range(0, 17):
        text += spalten[i]
        if (i == 16):
            break
        text += ', '

    # open CSV
    df = pd.read_csv("CSV/csv_sorted.csv", index_col=False, delimiter=',')

    # df = pd.read_csv("CSV/csv_sorted.csv")#, index_col=False, delimiter=',')
    # df = pd.read_csv("CSV/csvTest2.csv", index_col=False, delimiter=',')      # Hier wird die unsortierte CSV geöffnet -> In manchen Fällen besseres Ergebnis

    # reading values into table
    for i, row in df.iterrows():
        sql = f"INSERT IGNORE INTO Tabelle ({text}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        my_cursor.execute(sql, tuple(row) + (fach, doz))
    mydb.commit()

def get_table_data(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Tabelle")
    result = mycursor.fetchall()

    # Umwandlung von List[Tuple] in List[List]
    table_data = [list(row) for row in result]
    mycursor.close()
    return table_data

def get_column_names(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Tabelle LIMIT 0")
    column_names = [i[0] for i in mycursor.description]
    mycursor.fetchall()
    mycursor.close()
    return column_names

def loesche_spalte(mydb, column_name):
    mycursor = mydb.cursor()
    query = f'ALTER TABLE Tabelle DROP COLUMN `{column_name}`'
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()

def add_column(mydb, column_name):
        mycursor = mydb.cursor()
        mycursor.execute(f"ALTER TABLE Tabelle ADD COLUMN `{column_name}` VARCHAR(255) DEFAULT '-'")
        mydb.commit()
        mycursor.close()