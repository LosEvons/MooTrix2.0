import cv2
import pytesseract
import PySimpleGUI as sg
import os.path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\emilm\AppData\Local\Tesseract-OCR\tesseract.exe'
def processing(useFileName):
    global svRead
    img = cv2.imread(useFileName)
    svRead = pytesseract.image_to_string(img, lang='eng+fin')
    return svRead
