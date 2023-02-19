import pytesseract
import cv2
from hocr_conf import *
from csv_sorte import *
from database import *
import PySimpleGUI as sg
import os

myconfig = r"--psm 6 --oem 3 --user-words custom_words.txt"


def processing(files, csv1, gui1):

    layout = [
        [sg.Text('processing data...')]
    ]
    load_screen = sg.Window('', layout, modal=True, finalize=True)
    # starting the whole process
    for x in files:

        load_screen.read(timeout=0)
        dir_path, file_name = os.path.split(x)
        print(f"Die derzeitige Datei in bearbeitung ist: {file_name}")

        text = text_extraction(x)
        csv1.converter(text, gui1)
        csv_sorte()

        fach = csv1.get_kurs()
        doz = csv1.get_dozent()
        # einlesen(fach, doz)
    load_screen.close()



def text_extraction(file):
    # Grayscale, Otsu's threshold
    image = cv2.imread(file)

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # invert image
    invert = 255 - thresh

    # Perform text extraction
    text = pytesseract.image_to_string(invert, lang='deu+tur', config=myconfig)
    # getting the hocr output for comparison
    hocr_output = pytesseract.image_to_pdf_or_hocr(invert, extension='hocr', lang='deu+tur', config=myconfig)
    hocr = hocr_output.decode('utf-8')

    with open('Texts/output.hocr', 'w') as f:
        f.write(hocr)

    hocr_conf()

    # cv2.imshow('invert', invert)
    # cv2.waitKey()

    # printing the extracted text before processing
    extracted_text = open("Texts/ausgabe.txt", "w")
    extracted_text.write(text)
    extracted_text.close()

    return text
