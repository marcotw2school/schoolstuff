from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Necessario solo se Tesseract non è nella PATH
lang = 'ita' # Prime tre lettere della lingua. Es: Inglese = eng
foto = 'fotoITA.png'

print(pytesseract.image_to_string(Image.open(foto), lang=lang))
