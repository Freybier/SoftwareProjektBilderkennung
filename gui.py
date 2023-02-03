import PySimpleGUI as sg


class Gui:
    dozent = ""
    kurs = ""

    def dateizug(self):
        sg.theme('Dark')

        layout = [[sg.Text('Name des Dozenten'), sg.InputText()],
                  [sg.Text('Kurs'), sg.InputText()],
                  [sg.Button('Upload')],
                  [sg.Button('Vergleich')],
                  [sg.Button('Ok')]]

        # layout = [[sg.Text('Name des Dozenten'), sg.InputText()],
        #           [sg.Text('Kurs'), sg.InputText()],
        #           [sg.FileBrowse(button_text="Upload"), sg.InputText("", key="-OUTPUT1-")],
        #           [sg.FileBrowse(button_text="Vergleich"), sg.InputText("", key="-OUTPUT2-")],
        #           [sg.Button('Ok')]]

        window = sg.Window('Bilderkennung', layout)

        while True:
            event, values = window.read()

            if event == 'Upload':
                self.files = self.filebrowser()
            if event == 'Vergleich':
                self.filebrowser2()
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
