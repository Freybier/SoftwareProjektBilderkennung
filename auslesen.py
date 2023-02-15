import pytesseract
import PIL.Image
import cv2
from vergleich import *
import numpy as np
from csv_converter import *
from csv_sorte import *

myconfig = r"--psm 6 --oem 3 --user-words custom_words.txt"

def vorbereitung(files, csv1, gui1):
    for x in files:
        text = auslese(x)
        csv1.converter(text, gui1)
        #csv_sorte()
        fach = csv1.get_kurs()
        doz = csv1.get_dozent()

        print(fach, doz)


def auslese(file):
    # Grayscale, Otsu's threshold
    image = cv2.imread(file)

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # invert image
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    invert = 255 - thresh

    # custom word list
    with open('custom_words.txt', 'w') as f:
        f.write(
            'mtknr\nsortname\nbewertung\npstatus\npversuch\nktxt\nspversion\nsemester\npdatum\npnr\nbonus\nlabnr\npordnr\nporgnr\nMail\nstartHISsheet\nendHISsheet\nÇakar\nM-IIM')

    # Perform text extraction

    text = pytesseract.image_to_string(invert, lang='deu+tur', config=myconfig)

    hocr_output = pytesseract.image_to_pdf_or_hocr(invert, extension='hocr', lang='deu+tur', config=myconfig)
    hocr = hocr_output.decode('utf-8')

    with open('output.hocr', 'w') as f:
        f.write(hocr)

    vergl = open("Texts/demo.txt", "w")
    vergl.write(text)
    vergl.close()

    return text
