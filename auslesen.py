import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 6 --oem 3"


def auslese(file):
    #text = pytesseract.image_to_string(PIL.Image.open(file), config=myconfig, lang="deu")
    #print(text)

    # Grayscale, Otsu's threshold
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    #invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    invert = 255 - thresh

    # Perform text extraction
    text = pytesseract.image_to_string(invert, lang='deu', config=myconfig)
    print(text)

    cv2.imshow('thresh', thresh)
    cv2.imshow('image', image)
    cv2.imshow('invert', invert)
    cv2.waitKey()

    return text


