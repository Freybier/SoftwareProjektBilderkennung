import re


def convert(text):
    csv_converted = open("CSV/csvTest.csv", "w")

    lines = text.split("\n")
    counter_lines = 0
    first_line = True

    for line in lines:
        if first_line:
            first_line = False
            fach_dozent(line)
            continue
        words = lines[counter_lines].split()
        counter_lines = counter_lines + 1
        counter_words = 0
        name_tag = False
        name = ""
        if line == "":
            continue
        if re.search(line, "startHissheet endHissheet", re.IGNORECASE) or re.search(line, "endHissheet.",
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
        csv_converted.write("\n")
    csv_converted.close()


def fach_dozent(line):
    first, *middle, last = line.split()
    dozent = last
    kurs = first
    for word in middle:
        kurs = kurs + " " + word


