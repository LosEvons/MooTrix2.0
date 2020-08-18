import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [  [sg.Text('Choose a file to process')],
            [sg.Text("File Folder"),
             sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
             sg.FileBrowse()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('MooTrix', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


window.close()
