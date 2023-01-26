def sorting_cheeses(**kwargs):
    sorted_lst = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []

    for type, pieces in sorted_lst:
        result.append(type)
        result.extend(sorted(pieces, reverse=True))
    return '\n'.join(str(x) for x in result)

print(
sorting_cheeses(
Parmesan=[102, 120, 135],
Camembert=[100, 100, 105, 500, 430],
Mozzarella=[50, 125],
)
)