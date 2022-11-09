
def convert(text):
    csv_converted = open("CSV/csvTest.csv", "w")

    # Versuch mit Wörtern
    lines = text.split("\n")
    counter_lines = 0

    for line in lines:
        words = lines[counter_lines].split()
        counter_lines = counter_lines + 1
        counter_words = 0
        name_tag = False
        name = ""
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
