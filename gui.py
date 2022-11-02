import PySimpleGUI as sg


def dateizug():

    filename = sg.popup_get_file('Geben Sie eine Bilddatei an', multiple_files=True)
    files = filename.split(';')
    return files
