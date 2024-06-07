import cv2
import pytesseract
def IMAGES(path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(path)
    img_text = pytesseract.image_to_string(img).lower().replace('\n', ' ')
    return img_text
