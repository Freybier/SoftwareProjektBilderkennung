"""
def text_vergleich(original_pfad, vergleich_pfad):
    counter = 0
    original = open(original_pfad, "r")
    vergleichstext = open(vergleich_pfad, "r")

    for o_line in original.readlines():
        v_line = vergleichstext.readline()

        print(o_line +"\n" + v_line + "\n\n")

        if len(o_line) != len(v_line):
            print("unterschiedliche Länge der Zeile")
            if len(o_line) > len(v_line):
                print("Hier fehlt was")
        else:
            for x, y in zip(o_line, v_line):
                if x != y:
                    if x == "\t" and y == " " or x == " " and y == "\t":
                        continue
                    print("Fehler")
                    counter = counter + 1

"""

def compare_files(file1, file2):
    # with open(file1, "r") as f1, open(file2, "r") as f2:
    #     lines1 = f1.readlines()
    #     lines2 = f2.readlines()
    #     counter = 0
    #
    #     if len(lines1) != len(lines2):
    #         print("Zeilen sind nicht gleich lang")
    #     for line1, line2 in zip(lines1, lines2):
    #         if line1 != line2:
    #             # Vergleich der Zeichen in der aktuellen Zeile
    #             for char1, char2 in zip(line1, line2):
    #                 if char1 != char2:
    #                     print(f"Unterschied bei Zeichen {char1} und {char2} in Zeile {line1}")
    #                     counter = counter + 1
    #     return counter

    original = open(file1, "r")
    scan = open(file2, "r")

    kill_newLines(original, "vergleich_original")
    kill_newLines(scan, "vergleich_scan")

    counter = 0
    for o_line in original.readlines():
        s_line = scan.readline()

        o_w_line = o_line.split()
        s_w_line = s_line.split()

        if len(o_w_line) < len(s_w_line):
            print("Es ist ein Wort zu viel" + s_line)
            #funktioniert so nicht, ich muss in diesem fall word2 um 1 erhöhen um den fehler auszugleichen
            for word1, word2 in zip(o_w_line, s_w_line):
                if word1 != word2:
                    print(word2 + " ist zu viel")
                    counter = counter + 1


        for i in range(min(len(o_w_line), len(s_w_line))):
            if o_w_line[i] != s_w_line[i]:
                print("Fehler in Zeile: " + s_line + " im Wort " + s_w_line[i] + "\n")
                print("\n")
                counter += 1

    print(f"Es gibt insgesamt {counter} Fehler")


def kill_newLines(text, name):

    datei = open(f"Texts/{name}.txt", "w")

    for line in text:
        if line == "\n":
            continue
        datei.write(line)






















def csv_vergleich():
    counter = 0
    original = open("CSV/tabelle8.csv", "r")
    eingelesen = open("CSV/csvTest.csv", "r")

    for o_line in original.readlines():
        v_line = eingelesen.readline()

        if o_line != v_line:
            print("Es gibt einen Fehler in Zeile " + v_line)
            counter = counter + 1

            for x, y in zip(o_line, v_line):
                if x != y:

                    print("Fehler in Zeile " + o_line)
                    print(x)

    print(f"Es gibt insgesamt {counter} Fehler")