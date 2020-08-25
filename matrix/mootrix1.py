import csv
from collections import Counter
import unicodedata
import pytesseract
import os.path
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\emilm\AppData\Local\Tesseract-OCR\tesseract.exe'
#Opens the file
def fileopen(svRead, useFileName):
    print("File from: "+useFileName+" opened")
    if useFileName.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Your file is a picture, trying to extract text...")
        #If file is a picture, process it into text
        processing(useFileName)
        print("Text extracted. Saving a text file...")
        txtMaker(dirName, customName, svRead)
    else:
        #Otherwise just open the damn thing, and casefold it
        sv = open(useFileName, 'r', encoding="UTF-8")
        svRead = sv.read()
        sv.close()
    svRead = svRead.casefold()
    print("Total characters in file: ")
    print(len(svRead))
    return svRead

def parseAlnum(svRead, svParsed, inclusionList):
    #parses all non-alphanumeric UTF-8 characters out
    for char in svRead:
        charCode = ord(char)
        if char.isalnum() or char in inclusionList:
            if 8192 <= charCode <= 8303:
                #this checks a range of UTF-8 characters that includes punctuation that the isalnum() doesn't catch
                svParsed += char
        else:
            continue
    print("Total characters in parsed file: ")
    print(len(svParsed))
    return svParsed

def listMaker(svParsed):
    #this makes a list out of every worrd in the parsed textfile
    svSplit = re.split(" |\n", svParsed)
    cnt = Counter(svSplit)
    print("Total number of words detected: ")
    print(len(cnt))
    return cnt

def txtMaker(dirName, customName, svRead):
    #used to output a text file of the picture. This is for troubleshooting and double checking purposes.
    with open(dirName+'/'+customName+'.txt', 'w') as textfile:
        textfile.write(svRead)

def csvMaker(dirName, customName, cnt):
    #This makes the end product(a csv-file)
    cntCommon = cnt.most_common()
    cntWrite = Counter(dict(cntCommon))
    with open(dirName+'/'+customName+'.csv', 'w', newline='', encoding="UTF-8") as csvfile:
        fieldnames = ['Word', 'Wordcount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tag, count in cntWrite.items():
            writer.writerow({'Word': tag, 'Wordcount': str(count)})
    print("Length of cnt: ")
    print(len(cnt))
    print("Length of cntWrite ")
    print(len(cnt))

def processing(useFileName):
    #This is used for getting text out of images
    img = cv2.imread(useFileName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    svRead = pytesseract.image_to_string(gray, land='eng+fin')
    return svRead
