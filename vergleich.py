
def vergleich_csv_text():
    # Lesen der beiden Vergleichsdateien
    with open("Texts/csvText.txt") as input_file, open("Texts/vergleich_csv.txt", "w") as output_file:
        for line in input_file:
            if line.strip():  # überprüft, ob die Zeile Inhalt hat
                output_file.write(line)

    with open("Texts/vergleich_csv.txt", "r") as file1, open("Texts/vergleich_text.txt", "r") as file2:
        content1 = file1.readlines()
        content2 = file2.readlines()

    # Zählen der übereinstimmenden Wörter
    num_correct = 0
    num_total = 0
    error_lines = []
    for i, (line1, line2) in enumerate(zip(content1, content2)):
        if not line1.strip() or not line2.strip():
            continue
        words1 = line1.strip().split()
        words2 = line2.strip().split()
        num_total += len(words1)
        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                num_correct += 1
            else:
                error_lines.append(f"Line {i+1}: expected '{word2}', but got '{word1}'")

    # Schreiben der Fehler in eine neue Datei
    with open("Texts/vergleich_error.txt", "w") as error_file:
        error_file.write("\n".join(error_lines))

    # Ausgabe der Ergebnisse
    correct_ratio = num_correct / num_total
    print(f"Die Gesamtzahl an Fehlern beträgt: {num_total - num_correct}")
    print(f"Richtige Auslese: {correct_ratio:.2%}")

def hocr_vergleich():
    with open("output.hocr", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "<span class='ocrx_word'" in line:
                start_index = line.find("x_wconf") + 8
                end_index = line.find("'", start_index)
                x_wconf = int(line[start_index:end_index])
                if x_wconf < 80:
                    word_start = line.find(">") + 1
                    word_end = line.find("<", word_start)
                    word = line[word_start:word_end]
                    print(f"x_wconf: {x_wconf}, Word: {word}")

    with open("output.hocr", "r") as file:
        lines = file.readlines()
        with open("hocr-confidence.txt", "w") as confidence_file:
            for line in lines:
                if "<span class='ocrx_word'" in line:
                    start_index = line.find("x_wconf") + 8
                    end_index = line.find("'", start_index)
                    x_wconf = int(line[start_index:end_index])
                    if x_wconf < 80:
                        word_start = line.find(">") + 1
                        word_end = line.find("<", word_start)
                        word = line[word_start:word_end]
                        confidence_file.write(f"x_wconf: {x_wconf}, Word: {word}\n")

    vergleich_csv_text()