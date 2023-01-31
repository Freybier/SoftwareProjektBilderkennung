import re
import csv

class CSVObject:

    counter_input = 0
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

                if word.endswith(".de") and len(words) != counter_spalten+1:
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
            with open("CSV/csvTest.csv", "r") as my_input_file:
                [my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
            my_output_file.close()