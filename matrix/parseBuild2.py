"""        if char in exceptionList:
            newChar = char.replace(char, '')
            svParsed += newChar
        elif char.casefold() not in exceptionList:
            svParsed += char
        else:
            continue
"""

#imports
import csv
import string
import re
from collections import Counter
import unicodedata
import PySimpleGUI as sg
import os
import someFile
#Fileopen
def fileopen():
    startWindow()
    if useFileName.lower().endswith(('.png', '.jpg', '.jpeg')):
        someFile.processing(useFileName)
    else:
        global svRead
        sv = open(useFileName, 'r', encoding="UTF-8")
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
svParsed2 = ''
svRead = ''
#listmaker
def listmaker(cnt, svParsed, svParsed2, svRead, exceptionList):
    for char in svRead:
        if char.isalnum() or char == ' ' or char == '\n':
            svParsed += char
    for char in svRead:
        if char.casefold() in exceptionList:
            newChar = char.replace(char, '')
            svParsed2 += newChar
        elif char.casefold() not in exceptionList:
            svParsed2 += char

    print("svParsed and svParsed2 values:")
    print(len(svParsed))
    print(len(svParsed2))
    for char in svParsed2:
        if char not in svParsed:
            print(char)
    for word in re.split(" |\n", svParsed):
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word] = 1

    with open(dirName+'/'+customName+'.txt', 'w') as textfile:
        textfile.write(svRead)
    textfile.close()

    with open(dirName+'/'+customName+'.cfg', 'w', newline='', encoding='UTF-8') as csvfile:
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

#GUI
def startWindow():
    global customName
    global useFileName
    global dirName
    sg.theme('BluePurple')
    layout = [[sg.Text('Input', size=(9,1)), sg.Input(key='-FILEIN-'), sg.FileBrowse()],
            [sg.Text('Result', size=(9,1)), sg.Input(key='-FILENAME-')],
            [sg.Text('Save', size=(9,1)), sg.Input(key='-FILEOUT-'), sg.FolderBrowse()],
            [sg.Submit(), sg.Cancel()]]
    window = sg.Window('MooTrix', layout)
    event, values = window.read()
    useFileName = values['-FILEIN-']
    customName = values['-FILENAME-']
    dirName = values['-FILEOUT-']
    return customName
    return useFileName
    return dirName
    window.close()
#Checks and initiation
fileopen()
print(len(svRead))
listmaker(cnt, svParsed, svParsed2, svRead, exceptionList)
print("starting to rank words...")
print("Most used words:")
print("\n")
print("Writing a CSV-File...")
print("CSV-file written!")
print("Shutting down...")
