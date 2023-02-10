import PySimpleGUI as sg
import threading
from auslesen import *


class Gui:
    dozent = ""
    kurs = ""

    def __init__(self):
        sg.theme('Dark')
        layout = [[sg.Text('Name des Dozenten'), sg.InputText()],
                  [sg.Text('Kurs', pad=((5, 98), (0, 0))), sg.InputText(), sg.Button('Aktualisieren')],
                  [sg.Text('Bilddateien', pad=((5, 62), (0, 0))), sg.InputText('', key='-FILES-'), sg.Button('Upload')],
                  [sg.Button('Vergleich'), sg.InputText('', key='-TEXT-')],
                  [sg.Column(layout=[[sg.Button('Datenbank', pad=((5, 345), (0, 0))), sg.Button('Ok'), sg.Button('Cancel')]],
                             pad=((0, 0), (70, 0)))]]

        self.window = sg.Window('Bilderkennung', layout, size=(600, 250))

    def dateizug(self, csv1):

        sg.theme('Dark')

        while True:
            event, values = self.window.read()

            if event == 'Upload':
                self.files = self.filebrowser()
                self.window['-FILES-'].update("{}".format(self.files))
            if event == 'Vergleich':
                self.filebrowser2()
                self.window['-TEXT-'].update("{}".format("Texts/vergleich_text.txt"))
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            if event == 'Aktualisieren':
                self.dozent = values[0]
                self.kurs = values[1]
                sg.popup_ok("Kurs und Dozent wurden aktualisiert")
            if event in (sg.WIN_CLOSED, 'Ok'):
                self.dozent = values[0]
                self.kurs = values[1]
                thread = threading.Thread(target=vorbereitung(self.files, csv1, self))
                thread.start()
        # window.close()

    def filebrowser(self):
        filename = sg.popup_get_file('Geben Sie eine Bilddatei an', multiple_files=True)
        if filename is not None:
            files = filename.split(';')
            return files
        else:
            print("Ich hab keine Datei")
            filename = "Trash_Images/test_text.png"
            files = filename.split(';')
            return files

    def filebrowser2(self):
        txt_filename = sg.popup_get_file('Geben Sie eine Textdatei an', multiple_files=True)
        if txt_filename is not None:
            with open("Texts/vergleich_text.txt", "w") as file:
                with open(txt_filename, "r") as selected_file:
                    file.write(selected_file.read())
        else:
            print("Ich hab keine Datei")
            txt_filename = "Texts/demo_vergleich.txt"
            with open("Texts/vergleich_text.txt", "w") as file:
                with open(txt_filename, "r") as demo_file:
                    file.write(demo_file.read())

    def get_dozent(self):
        return self.dozent

    def get_kurs(self):
        return self.kurs
