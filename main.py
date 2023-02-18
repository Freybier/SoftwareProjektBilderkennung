from gui import *
from auslesen import *
from database import *


initialize_database()
loesche_tabelle("Tabelle")
erstelle_tabelle("Tabelle")

csv1 = CSVObject()
gui1 = Gui()
gui1.dateizug(csv1)
