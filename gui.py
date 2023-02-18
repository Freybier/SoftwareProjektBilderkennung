import PySimpleGUI as sg
import threading
from auslesen import *
from vergleich import *
from database import *


class Gui:
    dozent = ""
    kurs = ""

    def __init__(self):
        sg.theme('Dark')
        layout = [[sg.Text('Name des Dozenten'), sg.InputText()],
                  [sg.Text('Kurs', pad=((5, 98), (0, 0))), sg.InputText(), sg.Button('Aktualisieren', size=(15, 0))],
                  [sg.Text('Bilddateien', pad=((5, 61), (0, 0))), sg.InputText('', key='-FILES-'), sg.Button('Upload', size=(15, 0))],
                  [sg.Text('Vergleichsdaten', pad=((5, 32), (0, 0))), sg.InputText('', key='-TEXT-'), sg.Button('Vergleich', size=(15, 0))],
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
            if event == 'Ok':
                self.dozent = values[0]
                self.kurs = values[1]
                auslesen = threading.Thread(target=vorbereitung(self.files, csv1, self))
                auslesen.start()
                vergleichen = threading.Thread(target=hocr_vergleich())
                vergleichen.start()
            if event == 'Datenbank':
                datenB = threading.Thread(target=self.build_datenbank_gui())
                datenB.start()
        self.window.close()

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

    def build_datenbank_gui(self):
        # Verbindung zur Datenbank herstellen
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="notenuebersicht",
            password="password"
        )

        sg.theme('Dark')

        # Suchfeld hinzufügen
        search_input = sg.InputText(key='search')
        search_button = sg.Button('Suchen')

        # Schaltfläche zum Hinzufügen einer Spalte hinzufügen
        add_column_input = sg.InputText(key='column_name')
        add_column_button = sg.Button('Spalte hinzufügen')

        # Button zum Löschen der Spalten
        drop_column_button = sg.Button('Spalte löschen')

        # Spaltenüberschriften und Tabelleninhalt hinzufügen
        columns = get_column_names(mydb)
        table_data = get_table_data(mydb)
        table_layout = [[search_input, search_button],
                        [add_column_input, add_column_button, drop_column_button],
                        [sg.Table(values=table_data, headings=columns, num_rows=10,
                                  auto_size_columns=True, key='-TABLE-')]]

        # Fenster erstellen
        db_window = sg.Window('Datenbank', table_layout)

        # Schleife zum Aktualisieren der Tabelle basierend auf der Suche
        while True:
            event, values = db_window.read()
            if event == sg.WIN_CLOSED:
                break

            # Suchen-Button auswerten
            if event == 'Suchen':
                search_term = values['search']
                filtered_data = [row for row in get_table_data(mydb) if search_term.lower() in str(row).lower()]
                db_window['-TABLE-'].update(values=filtered_data)

            # Schaltfläche zum Hinzufügen einer Spalte auswerten
            if event == 'Spalte hinzufügen':
                column_name = values['column_name']
                add_column(mydb, column_name)

                # Spaltenüberschriften aktualisieren
                columns = get_column_names(mydb)

                # Tabellen-Element mit aktualisierten Daten und Spaltenüberschriften neu erstellen
                table_data = get_table_data(mydb)
                table = db_window['-TABLE-']
                table.update(values=table_data)
                db_window.close()

            if event == 'Spalte löschen':
                # l_spalte = threading.Thread(target=lambda: self.db_loeschen(get_column_names(mydb)))
                # l_spalte.start()
                l_spalte = self.db_loeschen(get_column_names(mydb))
                for i in l_spalte:
                    loesche_spalte(mydb, i)
                db_window.close()

        db_window.close()

    def db_loeschen(self, spalten):

        layout = [
            [sg.Text('Löschbare Elemente der Tabelle')],
            [sg.Listbox(spalten, size=(20, 15), key='SELECTED', enable_events=True, select_mode='extended')],
            [sg.Button('Löschen')],
        ]

        window = sg.Window('Spalte löschen', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Löschen':
                break

        window.close()

        if values and values['SELECTED']:
            return values['SELECTED']
