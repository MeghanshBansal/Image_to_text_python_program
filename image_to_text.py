import argparse
import re

import PyPDF2
import cv2
import pytesseract

# taking argument from the command line
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help='image path with name')
args = vars(parser.parse_args())

# reading image and adding the preprocessing
if re.search(r'.pdf', args['image']):
    obj = open(args['image'], 'rb')
    pdfreader = PyPDF2.PdfFileReader(obj)
    for i in range(pdfreader.numPages):
        pageObj = pdfreader.getPage(i)
        print(pageObj.extractText())
    obj.close()
else:
    gray = cv2.imread(args['image'], 0)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # applying ocr with tesseract
    text = pytesseract.image_to_string(gray)
    print("\n\n\n")
    print(text, '\n\n\n')

    file = open('image_text.txt', 'w')
    file.write(text)
    
