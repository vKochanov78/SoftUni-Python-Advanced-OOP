occurrences = {}

for letter in input():
    if letter not in occurrences:
        occurrences[letter] = 0
    occurrences[letter] += 1

for l, c in sorted(occurrences.items()): # l -> letter, c -> count
    print(f'{l}: {c} time/s')