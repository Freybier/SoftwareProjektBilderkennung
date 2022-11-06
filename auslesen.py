import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 6 --oem 3"


def auslese(file):
    text = pytesseract.image_to_string(PIL.Image.open(file), config=myconfig, lang="deu")
    print(text)
    #text = pytesseract.image_to_data(file, output_type='data.frame')
    return text


