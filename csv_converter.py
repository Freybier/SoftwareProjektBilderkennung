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

    def convert(self, text, gui):
        csv_converted = open("CSV/csvTest.csv", "w")
        lines = text.split("\n")
        counter_lines = 0

        counter_spalten = 0

        first_line = True

        for line in lines:
            if first_line:
                if gui.get_kurs() != "" and gui.get_dozent() != "":
                    first_line = False
                    self.kurs = gui.get_kurs()
                    self.dozent = gui.get_dozent()
                    counter_lines = counter_lines + 1
                    continue
                else:
                    first_line = False
                    self.fach_dozent(line)
                    counter_lines = counter_lines + 1
                    continue
            words = lines[counter_lines].split()
            counter_lines = counter_lines + 1
            counter_words = 0

            name_tag = False
            name = ""
            if line == "":
                continue

            prev_word = ""

            for word in words:
                if word == "mtknr":
                    counter_spalten = len(words)
                    print(f"Es sollen {counter_spalten} spalten sein")

                if word.endswith(".de") and len(words) != counter_spalten + 1:
                    print(f"{word} ist die e-mail addresse")
                    csv_converted.write(f"\"{prev_word}" + f"{word}\",")
                    counter_words = counter_words + 1
                    break
                if word == "startHISsheet" or word == "endHISsheet":
                    break
                if word == "_" or word == "-" or word == "—" or word == "=":
                    counter_words = counter_words + 1
                    continue
                for char in word:
                    name_tag = False
                    if char == ",":
                        name_tag = True
                if name_tag:
                    name_tag = False
                    name = word
                    continue
                counter_words = counter_words + 1
                if name != "":
                    csv_converted.write(f"\"{name}" + " " + f"{word}\",")
                    name = ""
                    counter_words = counter_words + 1
                    continue
                if word == 'o':
                    csv_converted.write('"0",')
                    continue
                if counter_words != len(words):
                    csv_converted.write(f"\"{word}\",")
                else:
                    csv_converted.write(f"\"{word}\"")

                prev_word = word
            if len(lines) != counter_lines:
                csv_converted.write("\n")
                self.counter_input = self.counter_input + 1

        csv_converted.close()
        self.csv_to_txt()

    # toDo change python-for-loops into array based for loop, iterate through all words and check for mistakes before printing into csv-format
    def converter_neu(self, text, gui):
        csv_converted2 = open("CSV/csvTest2.csv", "w")
        lines = text.split("\n")
        first_line2 = True

        for line in lines:
            if line == "\n" or line == "":
                continue
            if first_line2 and lines[0] != "startHISsheet":
                if gui.get_kurs() != "" and gui.get_dozent() != "":
                    first_line2 = False
                    self.kurs = gui.get_kurs()
                    self.dozent = gui.get_dozent()
                    continue
                else:
                    first_line2 = False
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
                if words[i] == "mtknr":
                    self.counter_spalten = len(words)
                    print(f"Es sollen {self.counter_spalten} spalten sein")
            if words[i] == "" or words[i] is None:
                print("Hab ein None gefunden")
                continue
            # sorgt dafür, dass manche mails mit den Wörtern combiniert werden
            #nutz eine While schleife die bis die richtige anzahl an wörtern in der Zeile ist alle hinteren miteinander verbindet, damit kannst du dir auch den di+oppelten code sparen
            elif words[i].endswith(".de") and len(words) >= self.counter_spalten + 1:
                for char in words[i]:
                    if char == '&':
                        words[i] = words[i].replace('&', '@')
                ruckschritt = 1
                #möglichkeit zum fixen des None-Errors: einen words per line counter machen, davon die erste Schleife abhängig machen und alle werte die zu viel sind komplett poppen(ähnlich wie im ersten Versuch)
                while words[i-ruckschritt] is not None and words[i-ruckschritt].isdigit() is False:
                    words[i - ruckschritt] = f"{words[i - ruckschritt]}{words[i-(ruckschritt-1)]}"
                    words[i-(ruckschritt-1)] = None
                    ruckschritt = ruckschritt+1
                    #words = self.entferne_element(words, words[i])
            elif words[i].endswith(".de"):
                for char in words[i]:
                    if char == '&':
                        words[i] = words[i].replace('&', '@')
            elif words[i].lower() == "startHISsheet".lower() or words[i].lower() == "endHISsheet".lower() or words[
                i].lower() == "endHISsheet.".lower():
                return
            elif words[i] == "_" or words[i] == "-" or words[i] == "—" or words[i] == "=" or words[i] == " ":
                words[i] = None
            elif words[i] == "MM" or words[i] == 'MAM':
                words[i] = "M-IIM"
            elif words[i] == 'o' or words[i] == '°':
                words[i] = "0"
            elif words[i].endswith(","):
                words[i] = f"{words[i]} {words[i + 1]}"
                words[i + 1] = None
            elif words[i] == "kit" or words[i] == "kbrt" or words[i] == "kbxt":
                words[i] = "ktxt"
            elif words[i] == "par":
                words[i] = "pnr"
            if i == words[len(words)-1]:
                print(f"Die Zeile ist so fertig {words}")
                return words

        filtered_words = [word for word in words if word is not None]
        print(f"Die Zeile ist perfekt {filtered_words}")
        return filtered_words

    def entferne_element(self, words, element):
        element_to_delete = element
        words.remove(element_to_delete)
        for i in range(words.index(element), len(words) - 2):
            words[i] = words[i + 1]

        words.pop()
        return words

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
