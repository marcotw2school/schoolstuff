from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Necessario solo se Tesseract non è nella PATH
lang = 'ita' # Prime tre lettere della lingua. Es: Inglese = eng. Guarda: https://github.com/tesseract-ocr/tessdata
foto = 'foto.png'

testo = (pytesseract.image_to_string(Image.open(foto), lang=lang))
with open(foto + '.txt', "w") as file:  
    file.write(testo)
