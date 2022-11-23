import PySimpleGUI as sg


class Gui:

    dozent = ""
    kurs = ""


    def dateizug(self):
        sg.theme('DarkAmber')

        layout = [[sg.Text('Name des Dozenten'), sg.InputText()],
                  [sg.Text('Kurs'), sg.InputText()],
                  [sg.Button('Upload')],
                  [sg.Button('Ok')]]

        window = sg.Window('Bilderkennung', layout)

        while True:
            event, values = window.read()

            if event == 'Upload':
                self.files = self.filebrowser()
            if event in (sg.WIN_CLOSED, 'Ok'):
                break
        self.dozent = values[0]
        self.kurs = values[1]
        window.close()

        return self.files


    def filebrowser(self):
        filename = sg.popup_get_file('Geben Sie eine Bilddatei an', multiple_files=True)
        if filename is not None:
            files = filename.split(';')
            return files
        else:
            print("Ich hab keine Datei")
            filename = "Images/test_text.png"
            files = filename.split(';')
            return files

    def get_dozent(self):
        return self.dozent

    def get_kurs(self):
        return self.kurs