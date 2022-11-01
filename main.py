import pytesseract
import PIL.Image

from vergleich import *

'''Hallo ich bin Yann'''
myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("Images/test_text.png"), config=myconfig, lang="deu")
#print(text)


file = open("demo.txt", "w")
file.write(text)

file.close()

vergleich(text)

