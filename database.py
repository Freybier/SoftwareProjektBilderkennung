# import mysql.connector
# from mysql.connector import Error
# import pandas as pd
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
#                         mtknr INTEGER DEFAULT NULL,
#                         sortname VARCHAR(60) NULL,
#                         bewertung INTEGER NULL,
#                         pstatus VARCHAR(5) NULL,
#                         pversuch INTEGER NULL,
#                         ktxt VARCHAR(8) NULL,
#                         spversion INTEGER NULL,
#                         semester INTEGER NULL,
#                         pdatum VARCHAR(12) NULL,
#                         pnr INTEGER NULL,
#                         bonus INTEGER NULL,
#                         labnr INTEGER NULL,
#                         pordnr INTEGER NULL,
#                         porgnr INTEGER NULL,
#                         MAIL VARCHAR(80) NULL,
#                         Fach VARCHAR(80) NULL,
#                         `Dozierende Person` VARCHAR(80) NULL
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
#     empdata = pd.read_csv("CSV/csvTest.csv", index_col=False, delimiter=',')
#     empdata.head()
#
#     # sql = """
#     #         INSERT INTO Tabelle (Fach, `Dozierende Person`) VALUES (
#     #         'Algorithmen',
#     #         'Cakar'
#     #         )%s,%s,
#     #         """
#     for i, row in empdata.iterrows():
#         sql = f"INSERT INTO Tabelle VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'{fach}','{doz}')"
#         my_cursor.execute(sql, tuple(row))
#         print("Record inserted")
#         my_db.commit()
#
#     # my_cursor.execute(sql)
#     # my_db.commit()
#
