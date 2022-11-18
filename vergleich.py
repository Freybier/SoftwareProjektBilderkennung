def vergleich(file):
    counter = 0
    original = open("Texts/tabelle4.txt", "r")
    vergleichstext = open("Texts/demo.txt", "r")

    for o_line in original.readlines():
        v_line = vergleichstext.readline()

        if v_line == "\n":
            v_line = vergleichstext.readline()
            #print("Leerzeile zu viel vor " + v_line)
            #print("\n")
            counter += 1

        o_w_line = o_line.split()
        v_w_line = v_line.split()

        if len(o_w_line) != len(v_w_line):
            #print("Es fehlt ein wort in Zeile: " + v_line)
            counter += 1

        for i in range(min(len(o_w_line), len(v_w_line))):
            if o_w_line[i] != v_w_line[i]:
                #print("Fehler in Zeile: " + v_line + " im Wort " + v_w_line[i] + "\n")
                #print("\n")
                counter += 1

    print(f"Es gibt insgesamt {counter} Fehler")


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
                if x != y :

                    print("Fehler in Zeile " + o_line)
                    print(x)

    print(f"Es gibt insgesamt {counter} Fehler")