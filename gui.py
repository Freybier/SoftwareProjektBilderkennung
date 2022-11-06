import PySimpleGUI as sg


def dateizug():
    sg.theme('DarkAmber')

    layout = [[sg.Text('Geben Sie die Anzahl der Reihen an'), sg.InputText()],
              [sg.Text('Geben Sie die Anzhal der Spalten an'), sg.InputText()],
              [sg.Button('Upload')],
              [sg.Button('Ok')]]

    window = sg.Window('Bilderkennung', layout)

    while True:
        event, values = window.read()

        if event == 'Upload':
            files = filebrowser()
        if event in (sg.WIN_CLOSED, 'Ok'):
            break
    print(values[0])
    print(values[1])
    window.close()

    return files


def filebrowser():
    filename = sg.popup_get_file('Geben Sie eine Bilddatei an', multiple_files=True)
    if filename is not None:
        files = filename.split(';')
        return files
    else:
        print("Ich hab keine Datei")
        filename = "Images/test_text.png"
        files = filename.split(';')
        return files
