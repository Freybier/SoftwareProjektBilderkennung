# import mysql.connector
# from mysql.connector import Error
# import pandas as pd
# import PySimpleGUI as sg
#
# def initialize_database():
#     # Verbindung mit Datenbank
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password"
#     )
#     my_cursor = my_db.cursor()
#
#     # Wenn es noch keine Datenbank mit dem Namen "notenuebersicht" gibt wird eine erstellt
#     my_cursor.execute("SHOW DATABASES LIKE 'notenuebersicht'")
#     result = my_cursor.fetchall()
#     x = []
#     if result == x:
#         my_cursor.execute("CREATE DATABASE notenuebersicht")
#
# def erstelle_tabelle(name):
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         database="notenuebersicht",
#         password="password"
#     )
#     my_cursor = my_db.cursor()
#     test = f"SHOW TABLES LIKE '{name}'"
#     my_cursor.execute(test)
#     result = my_cursor.fetchone()
#     if result:
#         x = 0;
#     else:
#         sql = f"""
#                     CREATE TABLE `{name}`(
#                         mtknr VARCHAR(255) DEFAULT NULL,
#                         sortname VARCHAR(255) NULL,
#                         bewertung VARCHAR(255) NULL,
#                         pstatus VARCHAR(255) NULL,
#                         pversuch VARCHAR(255) NULL,
#                         ktxt VARCHAR(255) NULL,
#                         spversion VARCHAR(255) NULL,
#                         semester VARCHAR(255) NULL,
#                         pdatum VARCHAR(255) NULL,
#                         pnr VARCHAR(255) NULL,
#                         bonus VARCHAR(255) NULL,
#                         labnr VARCHAR(255) NULL,
#                         pordnr VARCHAR(255) NULL,
#                         porgnr VARCHAR(255) NULL,
#                         mail VARCHAR(255) NULL,
#                         fach VARCHAR(255) NULL,
#                         `Dozierende Person` VARCHAR(255) NULL,
#                         PRIMARY KEY (mtknr, pdatum)
#                         )
#                 """
#         my_cursor.execute(sql)
#
# def loesche_tabelle(name):
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         database="notenuebersicht",
#         password="password"
#     )
#     my_cursor = my_db.cursor()
#     test = f"SHOW TABLES LIKE '{name}'"
#     my_cursor.execute(test)
#     result = my_cursor.fetchone()
#     if result:
#         my_cursor.execute(f"DROP TABLE {name}")
#
# def einlesen(fach, doz):
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         database="notenuebersicht",
#         password="password"
#     )
#     my_cursor = my_db.cursor()
#
#     spalten = ['mtknr','sortname','bewertung','pstatus','pversuch','ktxt','spversion','semester','pdatum','pnr','bonus','labnr','pordnr','porgnr','mail','fach','`Dozierende Person`']
#     text = ''
#
#     for i in range(0, 17):
#         text += spalten[i]
#         if (i == 16):
#             break
#         text += ', '
#
#     # df = pd.read_csv("CSV/csv_sorted.csv", index_col=False, delimiter=',')
#     df = pd.read_csv("CSV/csvTest2.csv", index_col=False, delimiter=',')
#
#     try:
#         for i, row in df.iterrows():
#             sql = f"INSERT IGNORE INTO Tabelle ({text}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#             my_cursor.execute(sql, tuple(row) + (fach, doz))
#
#         my_db.commit()
#     except my_db.Error as e:
#         print(f"Error in row {i} adding entry to database: {e}")
#     # sql = """SELECT * FROM Tabelle;"""
#     # my_cursor.execute(sql)
#     #
#     # myresult = my_cursor.fetchall()
#     #
#     # for x in myresult:
#     #     print(x)
#
# def suche(suchbegriff):
#     # Verbindung zur Datenbank herstellen
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         database="notenuebersicht",
#         password="password"
#     )
#     my_cursor = my_db.cursor()
#
#     # Abfrage erstellen und ausführen
#     query = "SELECT * FROM Tabelle WHERE sortname LIKE '%{}%'".format(suchbegriff)
#     my_cursor.execute(query)
#
#     # Ergebnisse auslesen
#     result = my_cursor.fetchall()
#
#     # Verbindung zur Datenbank schließen
#     my_db.close()
#
#     # Ergebnisse ausgeben
#     for i in result:
#         print(i)
#
# def gethead():
#     # Verbindung zur Datenbank herstellen
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         database="notenuebersicht",
#         password="password"
#     )
#     my_cursor = my_db.cursor()
#
#     # df = pd.read_csv("CSV/csvTest2.csv", index_col=False, delimiter=',')
#
#     sql = """
#             SELECT `COLUMN_NAME`
#             FROM `INFORMATION_SCHEMA`.`COLUMNS`
#             WHERE `TABLE_SCHEMA`='notenuebersicht'
#             AND `TABLE_NAME`='Tabelle';
#             """
#     my_cursor.execute(sql)
#     df = my_cursor.fetchall()
#
#     spalten = []
#     # iterating the columns
#     for col in df:
#         print(col)
#         spalten.append(col)
#
#     # return spalten
#
# def build_datenbank_gui():
#     # Verbindung zur Datenbank herstellen
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="notenuebersicht"
#     )
#
#     # Funktion zum Abrufen der Spaltennamen
#     def get_column_names():
#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT * FROM Tabelle LIMIT 0")
#         column_names = [i[0] for i in mycursor.description]
#         mycursor.fetchall()  # Abrufen aller Zeilen, bevor der Cursor geschlossen wird
#         mycursor.close()
#         return column_names
#
#     # Funktion zum Abrufen der Tabelle
#     def get_table_data():
#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT * FROM Tabelle")
#         rows = mycursor.fetchall()
#         mycursor.close()
#         return rows
#
#     # GUI-Funktion zum Erstellen des Fensters
#     def build_datenbank_gui():
#         sg.theme('DarkAmber')
#
#         # Suchfeld hinzufügen
#         search_input = sg.InputText(key='search')
#         search_button = sg.Button('Suchen')
#
#         # Tabelleninhalt hinzufügen
#         table_layout = [[search_input, search_button],
#                         [sg.Table(values=get_table_data(), headings=get_column_names(), num_rows=10,
#                                   auto_size_columns=True, key='-TABLE-')]]
#
#         # Fenster erstellen
#         window = sg.Window('Datenbank', table_layout)
#
#         # Schleife zum Aktualisieren der Tabelle basierend auf der Suche
#         while True:
#             event, values = window.read()
#             if event == sg.WIN_CLOSED:
#                 break
#
#             # Suchen-Button auswerten
#             if event == 'Suchen':
#                 search_term = values['search']
#                 filtered_data = [row for row in get_table_data() if search_term.lower() in str(row).lower()]
#                 window['-TABLE-'].update(values=filtered_data)
#
#         window.close()
#
#     build_datenbank_gui()