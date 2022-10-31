import pytesseract
import PIL.Image
import cv2


myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("Images/test_text_punkt.png"), config=myconfig, lang="deu")
print(text)


file = open("demo.txt", "w")
file.write(text)
