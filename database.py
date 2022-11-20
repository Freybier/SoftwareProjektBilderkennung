def test(csv1):
    anzahl = csv1.get_anzahl_zeilen()
    print(anzahl)
    kurs = csv1.get_kurs()
    print(kurs)
    dozent = csv1.get_dozent()
    print(dozent)
# import mysql.connector
#
#
# def initialize_database():
#     my_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password"
#     )
#     my_cursor = my_db.cursor()
#     my_cursor.execute("SHOW DATABASES LIKE 'notenuebersicht'")
#     result = my_cursor.fetchall()
#
#     x = []
#
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
#                         mtknr INTEGER PRIMARY KEY ,
#                         sortname VARCHAR(60),
#                         bewertung INTEGER,
#                         pstatus VARCHAR(5),
#                         pversuch INTEGER,
#                         ktxt VARCHAR(8),
#                         spversion INTEGER,
#                         semester INTEGER,
#                         pdatum DATE,
#                         pnr INTEGER,
#                         bonus INTEGER,
#                         labnr INTEGER,
#                         pordnr INTEGER,
#                         porgnr INTEGER,
#                         MAIL VARCHAR(80)
#                     )
#                 """
#
#         my_cursor.execute(sql)
