# returns confidence values for each word, and prints it value below 80%
def hocr_conf():
    with open("Texts/output.hocr", "r") as file:
        lines = file.readlines()
        with open("Texts/hocr_confidence.txt", "w") as confidence_file:
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
