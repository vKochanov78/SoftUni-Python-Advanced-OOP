from string import  punctuation

with open("input.txt", "r") as input_file:
    text = input_file.readlines()

output_file = open("output.txt", "w")

for i in range(len(text)):
    letters = 0
    punct = 0

    row = text[i]

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punct += 1

    output_file.write(f"Line {i+1}: {row[:-1]} ({letters})({punct})\n")

output_file.close()