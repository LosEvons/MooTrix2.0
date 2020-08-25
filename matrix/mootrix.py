    #imports
import csv
import string
import re
from collections import Counter
import unicodedata
import pytesseract
import PySimpleGUI as sg
import os.path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\emilm\AppData\Local\Tesseract-OCR\tesseract.exe'

def listmaker(cnt, svParsed, svParsed2, svRead, exceptionList):
    for char in svRead:
        if char.isalnum() or char == ' ' or char == '\n':
            charCode = ord(char)
            if 8192 <= charCode <= 8303:
                svParsed += char
            else:
                continue
    for char in svRead:
        if char.casefold() in exceptionList:
            newChar = char.replace(char, '')
            svParsed2 += newChar
        elif char.casefold() not in exceptionList:
            svParsed2 += char

    for word in re.split(" |\n", svParsed):
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word] = 1

    with open(dirName+'/'+customName+'.txt', 'w') as textfile:
        textfile.write(svRead)
    textfile.close()

    with open(dirName+'/'+customName+'.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        cntCommon = cnt.most_common()
        cntWrite = Counter(dict(cntCommon))
        print(len(cnt))
        print(len(cntWrite))
        fieldnames = ['Word', 'Wordcount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tag, count in cntWrite.items():
            writer.writerow({'Word': tag, 'Wordcount': str(count)})
    csvfile.close()
    return cnt

def fileopen():
    startWindow()
    if useFileName.lower().endswith(('.png', '.jpg', '.jpeg')):
        processing(useFileName)
    else:
        sv = open(useFileName, 'r', encoding="UTF-8")
        svRead = sv.read()
        sv.close()
    svRead = svRead.casefold()
    print("Total characters in file:")
    print(len(svRead))
    return svRead

def processing(useFileName, svRead):
    img = cv2.imread(useFileName)
    svRead = pytesseract.image_to_string(img, lang='eng+fin')
    return svRead
