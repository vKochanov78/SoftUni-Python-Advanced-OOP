chemical_elements = set()

for _ in range(int(input())):
    for element in input().split():
        chemical_elements.add(element)

print(*chemical_elements, sep='\n')

