#imports
import csv
import string
import re
from collections import Counter
import unicodedata
import PySimpleGUI as sg
import os
#Fileopen
def fileopen():
    global svRead
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
cnt = Counter()
OrdCnt = Counter()
exceptionList = ["@", ",", ".", "!", ":", ";","-", "?", "»", "—", ""]
svParsed = ''
svRead = ''
#listmaker
def listmaker(cnt, svParsed, svRead, exceptionList):
    for char in svRead:
        if char.casefold() in exceptionList:
            newChar = char.replace(char, '')
            svParsed += newChar
        elif char.casefold() not in exceptionList:
            svParsed += char
        else:
            continue
    svParsed = svParsed.casefold()
    svParsed = svParsed.strip()
    for word in re.split(" |\n", svParsed):
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word] = 1

    secondWindow()
    print(dirName)
    filename = 'filematrix2.csv'
    with open(dirName+'/'+filename, 'w', newline='', encoding='UTF-8') as csvfile:
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

def secondWindow():
    global dirName
    dirName = sg.popup_get_folder('File save location')
    print(dirName)
    return dirName
#Checks and initiation
fileopen()
print(len(svRead))
print("foo")
listmaker(cnt, svParsed, svRead, exceptionList)
print("starting to rank words...")
print("Most used words:")
print("\n")
print("Writing a CSV-File...")
print("CSV-file written!")
print("Shutting down...")
