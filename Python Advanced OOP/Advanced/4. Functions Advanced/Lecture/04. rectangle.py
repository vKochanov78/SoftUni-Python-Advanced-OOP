def rectangle(length, wight):
    def area():
        return length * wight

    def perimeter():
        return (length + wight) * 2

    if type(length) != int or type(wight) != int:
        return "Enter valid values!"
    return f"""Rectangle area: {area()}
Rectangle perimeter: {perimeter()}"""

print(rectangle(2, 10))