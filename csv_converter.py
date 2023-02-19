import csv


class CSVObject:
    counter_input = 0
    counter_spalten = 0
    dozent = ""
    kurs = ""

    def __init__(self):
        self.counter_input = 0
        self.dozent = ""
        self.kurs = ""

    def converter(self, text, gui):
        csv_converted2 = open("CSV/csvTest2.csv", "w")
        lines = text.split("\n")
        first_line = True

        for line in lines:
            if line == "\n" or line == "" or line == " " or line == "\t":
                continue
            if first_line and lines[0] != "startHISsheet":
                if gui.get_kurs() != "" and gui.get_dozent() != "":
                    first_line = False
                    self.kurs = gui.get_kurs()
                    self.dozent = gui.get_dozent()
                    continue
                else:
                    first_line = False
                    self.fach_dozent(line)
                    continue
            bearbeitete_line = self.fehlerbereinigung(line)
            if bearbeitete_line != None:
                for x in range(len(bearbeitete_line)):
                    if x == len(bearbeitete_line) - 1:
                        csv_converted2.write(f"\"{bearbeitete_line[x]}\"")
                    else:
                        csv_converted2.write(f"\"{bearbeitete_line[x]}\",")
                csv_converted2.write("\n")

        csv_converted2.close()
        self.csv_to_txt()

    def fehlerbereinigung(self, line):
        words = line.split()
        for i in range(len(words)):
            if self.counter_spalten == 0:
                if words[i] == "Mail":
                    self.counter_spalten = len(words)
            if words[i] == "" or words[i] is None:
                continue
            elif words[i].endswith("."):
                words[i] = words[i].replace('.', '')
            elif words[i].endswith(".de"):
                for char in words[i]:
                    if char == '&':
                        words[i] = words[i].replace('&', '@')
                    elif char == '®':
                        words[i] = words[i].replace('®', '@')
            elif words[i].lower() == "startHISsheet".lower() or words[i].lower() == "endHISsheet".lower() \
                    or words[i].lower() == "endHISsheet.".lower():
                return
            elif words[i] == "_" or words[i] == "-" or words[i] == "—" or words[i] == "=" or words[i] == " ":
                words[i] = None
            elif words[i] == "MM" or words[i] == 'MAM' or words[i] == 'MIM' or words[i] == 'M-IM':
                words[i] = "M-IIM"
            elif words[i] == 'o' or words[i] == '°' or words[i] == 'a':
                words[i] = "0"
            elif words[i].endswith(","):
                words[i] = f"{words[i]} {words[i + 1]}"
                words[i + 1] = None
            elif words[i] == "kit" or words[i] == "kbrt" or words[i] == "kbxt" or words[i] == "kbit" or words[i] == "kbt":
                words[i] = "ktxt"
            elif words[i] == "mtkar":
                words[i] = "mtknr"
            elif words[i] == "par":
                words[i] = "pnr"
            if i == words[len(words) - 1]:
                return words
        filtered_words = [word for word in words if word is not None]
        final_words = self.len_check(filtered_words)
        return final_words

    def len_check(self, words):
        if len(words) == self.counter_spalten:
            return words
        else:
            final_array = []
            temp_array = []
            mail_finished = False
            differenz = len(words) - self.counter_spalten
            for i, word in enumerate(words):
                if mail_finished:
                    final_array.append(word)
                else:
                    temp_array.append(word)
                if word.endswith(".de"):
                    e_mail = ""
                    for j in range(differenz + 1):
                        e_mail = e_mail + words[i - differenz + j]
                        temp_array.pop()
                    for elem in temp_array:
                        final_array.append(elem)
                    final_array.append(e_mail)
                    mail_finished = True
            return final_array

    def fach_dozent(self, line):
        first, *middle, last = line.split()
        self.dozent = last
        self.kurs = first
        for word in middle:
            self.kurs = self.kurs + " " + word

    def get_anzahl_zeilen(self):
        return self.counter_input

    def get_anzahl_spalten(self):
        return self.counter_spalten

    def get_dozent(self):
        return self.dozent

    def get_kurs(self):
        return self.kurs

    def csv_to_txt(self):
        with open("Texts/csvText.txt", "w") as my_output_file:
            with open("CSV/csvTest2.csv", "r") as my_input_file:
                [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
            my_output_file.close()
