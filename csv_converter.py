import re


class CSVObject:

    counter_input = 0
    dozent = ""
    kurs = ""

    def __init__(self):
        self.counter_input = 0
        self.dozent = ""
        self.kurs = ""

    def convert(self, text):
        csv_converted = open("CSV/csvTest.csv", "w")
        counter_input = 0
        lines = text.split("\n")
        counter_lines = 0

        first_line = True

        for line in lines:
            if first_line:
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
            if re.search(line, "startHissheet endHissheet", re.IGNORECASE) or re.search(line, "endHiSsheet.",
                                                                                        re.IGNORECASE):
                continue
            for word in words:
                if word == "_":
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
                if counter_words != len(words):
                    csv_converted.write(f"\"{word}\",")
                else:
                    csv_converted.write(f"\"{word}\"")
            if len(lines) != counter_lines:
                csv_converted.write("\n")
                self.counter_input = self.counter_input + 1

        csv_converted.close()

    def fach_dozent(self, line):
        first, *middle, last = line.split()
        self.dozent = last
        self.kurs = first
        for word in middle:
            self.kurs = self.kurs + " " + word

    def get_anzahl_zeilen(self):
        return self.counter_input

    def get_dozent(self):
        return self.dozent

    def get_kurs(self):
        return self.kurs
