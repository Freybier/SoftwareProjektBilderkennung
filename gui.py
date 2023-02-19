import PySimpleGUI as sg
import threading
from auslesen import *
from vergleich import *
from database import *


class Gui:
    dozent = ""
    kurs = ""

    def __init__(self):
        # creating the layout and window
        sg.theme('Dark')
        layout = [[sg.Text('Name des Dozenten'), sg.InputText()],
                  [sg.Text('Kurs', pad=((5, 98), (0, 0))), sg.InputText(), sg.Button('Aktualisieren', size=(15, 0))],
                  [sg.Text('Bilddateien', pad=((5, 61), (0, 0))), sg.InputText('', key='-FILES-'), sg.Button('Upload', size=(15, 0))],
                  [sg.Text('Vergleichsdaten', pad=((5, 32), (0, 0))), sg.InputText('', key='-TEXT-'), sg.Button('Vergleich', size=(15, 0))],
                  [sg.Text('Bei Problemen kann eine Änderung der Schriftgröße helfen. "15" hat sich als stabilste \nSchriftgröße herausgestellt.')],
                  [sg.Column(layout=[[sg.Button('Datenbank', pad=((5, 345), (0, 0))), sg.Button('Ok'), sg.Button('Cancel')]],
                             pad=((0, 0), (30, 0)))]]

        self.window = sg.Window('Bilderkennung', layout, size=(600, 250))

    def dateizug(self, csv1):

        sg.theme('Dark')
        # waiting for buttonpress
        while True:
            event, values = self.window.read()

            if event == 'Upload':
                self.files = self.filebrowser_image()
                self.window['-FILES-'].update("{}".format(self.files))
            if event == 'Vergleich':
                self.filebrowser_comparison()
                self.window['-TEXT-'].update("{}".format("Texts/vergleich_text.txt"))
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            if event == 'Aktualisieren':
                self.dozent = values[0]
                self.kurs = values[1]
                sg.popup_ok("Kurs und Dozent wurden aktualisiert")
            if event == 'Ok':
                self.dozent = values[0]
                self.kurs = values[1]
                # starts own threads for processing and comparing files
                auslesen = threading.Thread(target=processing(self.files, csv1, self))
                auslesen.start()
                vergleichen = threading.Thread(target=vergleich_csv_text())
                vergleichen.start()
            if event == 'Datenbank':
                # starts own thread for building the database-gui
                database_gui = threading.Thread(target=self.build_datenbank_gui())
                database_gui.start()
        self.window.close()

    def filebrowser_image(self):
        # opens new window to select files
        filename = sg.popup_get_file('Geben Sie eine Bilddatei an', multiple_files=True)
        if filename is not None:
            files = filename.split(';')
            return files
        else:
            print("Ich hab keine Datei")
            return

    def filebrowser_comparison(self):
        # opens new window to select files for comparison
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

    def build_datenbank_gui(self):
        # connecting to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="notenuebersicht",
            password="password"
        )

        sg.theme('Dark')

        # add search-field
        search_input = sg.InputText(key='search')
        search_button = sg.Button('Suchen')

        # adds column
        add_column_input = sg.InputText(key='column_name')
        add_column_button = sg.Button('Spalte hinzufügen')

        # add column-deletion-button
        drop_column_button = sg.Button('Spalte löschen')

        # creating layout and window
        columns = get_column_names(mydb)
        table_data = get_table_data(mydb)
        table_layout = [[search_input, search_button],
                        [add_column_input, add_column_button, drop_column_button],
                        [sg.Table(values=table_data, headings=columns, num_rows=10,
                                  auto_size_columns=True, key='-TABLE-')]]

        db_window = sg.Window('Datenbank', table_layout)

        # waiting for events
        while True:
            event, values = db_window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'Suchen':
                search_term = values['search']
                filtered_data = [row for row in get_table_data(mydb) if search_term.lower() in str(row).lower()]
                db_window['-TABLE-'].update(values=filtered_data)

            if event == 'Spalte hinzufügen':
                column_name = values['column_name']
                add_column(mydb, column_name)

                columns = get_column_names(mydb)

                # create new table with new values
                table_data = get_table_data(mydb)
                table = db_window['-TABLE-']
                table.update(values=table_data)
                db_window.close()

            if event == 'Spalte löschen':
                l_spalte = self.db_loeschen(get_column_names(mydb))
                if l_spalte == 0:
                    break
                else:
                    for i in l_spalte:
                        loesche_spalte(mydb, i)
                # Fenster schließen
                db_window.close()

        db_window.close()

    def db_loeschen(self, spalten):
        # creating layout and window
        layout = [
            [sg.Text('Löschbare Elemente der Tabelle')],
            [sg.Listbox(spalten, size=(20, 15), key='SELECTED', enable_events=True, select_mode='extended')],
            [sg.Button('Löschen')],
        ]

        window = sg.Window('Spalte löschen', layout)

        # waiting for events
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Löschen':
                break

        window.close()

        # return selected fields
        if values and values['SELECTED']:
            return values['SELECTED']
        else:
            return 0
