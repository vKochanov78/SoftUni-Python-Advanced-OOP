from re import findall


class InvalidNameError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MoreThanOneAtSymbols(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_LENGTH_OF_NAME = 4
valid_domains = [".com", ".bg", ".org", ".net"]

name_pattern = r"[\w+\.]+"
domain_pattern = r"\.[a-z]+"

while True:
    command = input()

    if command == "End":
        break

    email = command

    try:

        if len(findall(name_pattern, email)[0]) != len(email.split("@")[0]):
            raise InvalidNameError("Name can only contain: letters, numbers, underscores and dots")

        if len(email.split("@")[0]) <= MIN_LENGTH_OF_NAME:
            raise NameTooShortError("Name must be more than 4 characters")

        if email.count("@") == 0:
            raise MustContainAtSymbolError("Email must contain @")

        if email.count("@") > 1:
            raise MoreThanOneAtSymbols("Email must contain only one '@' symbol")

        if findall(domain_pattern, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following:\n{', '.join(valid_domains)}")

    except IndexError:
        print("Invalid email")

    else:
        print("Email is valid")