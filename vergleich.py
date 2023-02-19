
def vergleich_csv_text():
    # reads both files for comparison
    with open("Texts/csvText.txt") as input_file, open("Texts/vergleich_csv.txt", "w") as output_file:
        for line in input_file:
            if line.strip():  # checks if line has value
                output_file.write(line)

    with open("Texts/vergleich_csv.txt", "r") as file1, open("Texts/vergleich_text.txt", "r") as file2:
        content1 = file1.readlines()
        content2 = file2.readlines()

    # counts similar words
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

    # creates new file and writes differences
    with open("Texts/vergleich_error.txt", "w") as error_file:
        error_file.write("\n".join(error_lines))

    # prints results
    correct_ratio = num_correct / num_total
    print(f"Die Gesamtzahl an Fehlern beträgt: {num_total - num_correct}")
    print(f"Richtige Auslese: {correct_ratio:.2%}")
