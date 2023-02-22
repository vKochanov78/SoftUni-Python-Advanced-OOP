from collections import deque

textile = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

crafted_items = {}

while textile and medicaments:
    cloth = textile.popleft()
    med = medicaments.pop()

    sum_of_items = cloth + med

    if sum_of_items in items:
        if items[sum_of_items] not in crafted_items:
            crafted_items[items[sum_of_items]] = 0

        crafted_items[items[sum_of_items]] += 1

    elif sum_of_items > 100:
        diff = sum_of_items - 100
        element = medicaments.pop()
        if "MedKit" not in crafted_items:
            crafted_items["MedKit"] = 0

        crafted_items["MedKit"] += 1

        total_amount_to_add = element + diff
        medicaments.append(total_amount_to_add)

    elif sum_of_items not in items:
        med += 10
        medicaments.append(med)


if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textile:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

items_created = sorted(crafted_items.items(), key=lambda x: (-x[1], x[0]))

for item, count in items_created:
    print(f"{item} - {count}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")
if textile:
    print(f"Textiles left: {', '.join(str(x) for x in textile)}")