import PySimpleGUI as sg
from parseBuild2 import fileName
def firstWindow(fileName):
    fileName = sg.popup_get_file('File to open')
    print(fileName)
    return fileName
