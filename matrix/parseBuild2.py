#imports
import csv
import string
import re
from collections import Counter
import unicodedata
import PySimpleGUI as sg
import os
#Fileopen
def fileopen(svRead):
    firstWindow()
    sv = open(fileName, 'r', encoding="utf-8")
    svRead = sv.read()
    sv.close()
    svRead = svRead.lower()
    print("Total characters in file:")
    print(len(svRead))
    return svRead

#variables
svParsed = "svparsed is empty"
svTF = "svTF is empty"
cnt = Counter()
OrdCnt = Counter()
svRead = ''

#cleanup
svParsed = ""
svTF = ""
exceptionList = ["@", ",", ".", "!", ":", ";","-", "?", "»", "—",]
for char in svRead:
    if char.casefold() in exceptionList:
        newChar = char.replace(char, '')
        svParsed += newChar
    elif char.casefold() not in exceptionList:
        svParsed += char
    else:
        continue

#listmaker
def listmaker(svParsed, cnt):
    svParsed = svParsed.casefold()
    svParsed = svParsed.strip()
    for word in re.split(" |\n", svParsed):
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word] = 1

    with open('filematrix2.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        cntCommon = cnt.most_common()
        cntWrite = Counter(dict(cntCommon))
        fieldnames = ['Word', 'Wordcount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tag, count in cntWrite.items():
            writer.writerow({'Word': tag, 'Wordcount': str(count)})
    csvfile.close()

#GUI
def firstWindow():
    global fileName
    fileName = sg.popup_get_file('File to open')
    print(fileName)
    return fileName

#Checks and initiation
fileopen(svRead)
listmaker(svParsed, cnt)
print("starting to rank words...")
print("Most used words:")
print("\n")
print("Writing a CSV-File...")
print("CSV-file written!")
print("Shutting down...")
