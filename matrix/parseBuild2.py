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
    startWindow()
    sv = open(useFileName, 'r', encoding="utf-8")
    svRead = sv.read()
    sv.close()
    svRead = svRead.casefold()
    print("Total characters in file:")
    print(len(svRead))
    return svRead

#variables
svParsed = "svparsed is empty"
cnt = Counter()
exceptionList = ["@", ",", ".", "!", ":", ";","-", "?", "»", ""]
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

    svParsed = svParsed.strip()
    for word in re.split(" |\n", svParsed):
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word] = 1

    with open(dirName+'/'+customName, 'w', newline='', encoding='UTF-8') as csvfile:
        cntCommon = cnt.most_common()
        cntWrite = Counter(dict(cntCommon))
        fieldnames = ['Word', 'Wordcount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tag, count in cntWrite.items():
            writer.writerow({'Word': tag, 'Wordcount': str(count)})
    csvfile.close()

#GUI
def startWindow():
    global customName
    global useFileName
    global dirName
    sg.theme('BluePurple')
    layout = [[sg.Text('Input', size=(7,1)), sg.Input(key='-FILEIN-'), sg.FileBrowse()],
            [sg.Text('Result name', size=(7,1)), sg.Input(key='-FILENAME-')],
            [sg.Text('Save location', size=(7,1)), sg.Input(key='-FILEOUT-'), sg.FolderBrowse()],
            [sg.Submit(), sg.Cancel()]]
    window = sg.Window('MooTrix', layout)

    event, values = window.read()
    window.close()
    useFileName = values['-FILEIN-']
    customName = values['-FILENAME-']+'.csv'
    dirName = values['-FILEOUT-']
    return customName
    return useFileName
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
