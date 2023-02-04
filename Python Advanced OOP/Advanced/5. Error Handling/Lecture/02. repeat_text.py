text = input()

try:
    times = int(input())
    text = text * times

except ValueError:
    print("Variable times must be an integer")

else:
    print(text)