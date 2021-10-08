names = []

with open("Input/Names/invited_names.txt", "r") as file:
    for line in file:
        line_no_new_line = line.replace("\n", "")
        names.append(line_no_new_line)
    file.close()

with open("Input/Letters/starting_letter.txt", "r") as file:
    file_data = file.read()
    for name in names:
        new_letter = file_data.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_to_{name}", "w") as letter:
            letter.write(new_letter)



