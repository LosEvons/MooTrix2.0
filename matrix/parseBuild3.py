import mootrix1
import PySimpleGUI as sg
from collections import Counter
###########
svRead = ''
svParsed = ''
cnt = Counter()
inclusionList = [" ", "\n"]
sg.theme('BluePurple')
layout = [[sg.Text('Input', size=(9,1)), sg.Input(key='-FILEIN-'), sg.FileBrowse()],
        [sg.Text('Result', size=(9,1)), sg.Input(key='-FILENAME-')],
        [sg.Text('Save', size=(9,1)), sg.Input(key='-FILEOUT-'), sg.FolderBrowse()],
        [sg.Submit(), sg.Cancel()]]
print("Mootrix booting up...")
window = sg.Window('MooTrix', layout)
event, values = window.read()
window.close()
useFileName = values['-FILEIN-']
customName = values['-FILENAME-']
dirName = values['-FILEOUT-']

svRead = mootrix1.fileopen(svRead, useFileName)
print("Cleanup started")
svParsed = mootrix1.parseAlnum(svRead, svParsed, inclusionList)
print("Formatting file...")
cnt = mootrix1.listMaker(svParsed)
print("Exporting data...")
mootrix1.csvMaker(dirName, customName, cnt)
print("File exported, shutting down...")
