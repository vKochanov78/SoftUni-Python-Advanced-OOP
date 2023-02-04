def age_assignment(*args, **kwargs):
    names = []

    for letter, age in kwargs.items():
        current_person_name = ''

        for current_name in args:
            if current_name.startswith(letter):
                current_person_name = current_name
                break

        names.append(f"{current_person_name} is {age} years old.")

    return '\n'.join(sorted(names))


print(age_assignment("Peter", "George", G=26, P=19))

print()

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))