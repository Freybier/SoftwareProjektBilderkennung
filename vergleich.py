def vergleich(text):
    original = open("original_text.txt", "r")
    vergleichstext = open("demo.txt", "r")

    for o_line in original.readlines():
        v_line = vergleichstext.readline()
        o_w_line = o_line.split()
        v_w_line = v_line.split()

        if len(o_w_line) != len(v_w_line):
            #print("Fehler in Zeile: " + v_line)
            #print("Richtige Zeile: " + o_line)

            for i in range(min(len(o_w_line), len(v_w_line))):
                if(o_w_line[i] != v_w_line[i]):
                    print("Der Fehler ist in Zeile: " + v_line + " im Wort " + v_w_line[i] + "\n")
