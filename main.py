from gui import *
from auslesen import *
from database import *

#initialize_database()
#loesche_tabelle("Tabelle")
#erstelle_tabelle("Tabelle")

gui1 = Gui()
files = gui1.dateizug()

kurs_eingabe = gui1.get_kurs()
dozent_eingabe = gui1.get_dozent()

csv1 = CSVObject()



for x in files:
    text = auslese(x)
    csv1.convert(text, gui1)
    #compare_files("Texts/tabelle8.txt", "Texts/vergleich_test_tabelle8.txt")
    fach = csv1.get_kurs()
    doz = csv1.get_dozent()

    print(fach, doz)

    #einlesen(fach, doz)


"""
bild = cv2.imread("Images/test_text.png")
height, width, _ = bild.shape

boxes = pytesseract.image_to_boxes(bild, config=myconfig)
for box in boxes.splitlines():
    box = box.split(" ")
    bild = cv2.rectangle(bild, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

data = pytesseract.image_to_data(bild, config=myconfig, output_type=Output.DICT)
menge_boxes = len(data['text'])
for i in range(menge_boxes):
    if float(data['conf'][i]) > 80:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        bild = cv2.rectangle(bild, (x, y), (x + width, y + height), (0, 0, 255), 2)

cv2.imshow('Images/test_text.png', bild)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
