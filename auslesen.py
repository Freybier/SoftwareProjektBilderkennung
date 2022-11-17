import pytesseract
import PIL.Image
import cv2
from vergleich import *
import numpy as np
from csv_converter import *

myconfig = r"--psm 6 --oem 3"


def auslese(file):

    # Grayscale, Otsu's threshold
    image = cv2.imread(file)

    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # upper and lower limits
    white_lo = np.array([50, 50, 50])
    white_hi = np.array([120, 200, 200])
    
    #man könnte die mail adresse zuerst als schwarz masken, und dann alle anderen zwischenfarbtöne auf weiß
    mail_lo = np.array([5, 5, 5])
    mail_hi = np.array([200, 200, 255])

    # mask
    mail_mask = cv2.inRange(hsv, mail_lo, mail_hi)
    mask = cv2.inRange(hsv, white_lo, white_hi)

    # change image to white where not fully black
    image[mail_mask > 0] = (0, 0, 0)
    #image[mask > 0] = (255, 255, 255)
    """

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # invert image
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    invert = 255 - thresh

    # Perform text extraction
    text = pytesseract.image_to_string(invert, lang='deu', config=myconfig)
    convert(text)

    vergl = open("Texts/demo.txt", "w")
    vergl.write(text)
    vergl.close()
    # vergleich(vergl)

    #cv2.imshow('image', image)
    #cv2.imshow('gray', gray)
    #cv2.imshow('binary', thresh)
    #cv2.imshow('invert', invert)

    #cv2.waitKey()

    return text


