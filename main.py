import pytesseract
import PIL.Image
import cv2
from vergleich import *

"""Hallo ich bin Yann"""
myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("Images/test_text.png"), config=myconfig, lang="deu")
#print(text)


file = open("demo.txt", "w")
file.write(text)

file.close()

vergleich(text)

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

