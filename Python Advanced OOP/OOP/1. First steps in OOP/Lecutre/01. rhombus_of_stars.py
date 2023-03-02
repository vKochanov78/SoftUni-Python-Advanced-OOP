def print_func(stars, spaces):
    print(" " * spaces + "* " * stars)


def draw(size):
    for i in range(size):
        stars_info = i + 1
        spaces_info = size - i - 1
        print_func(stars_info, spaces_info)

    for i in range(size - 2, -1, -1):
        stars_info = i + 1
        spaces_info = size - i - 1
        print_func(stars_info, spaces_info)


size_of_rhombus = int(input())
draw(size_of_rhombus)