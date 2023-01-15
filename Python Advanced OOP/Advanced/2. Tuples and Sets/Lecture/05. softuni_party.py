reservation_codes = {input() for _ in range(int(input()))}

arrived_to_the_party = set()

while True:
    arrived = input()

    if arrived == "END":
        break

    elif arrived in reservation_codes:
        arrived_to_the_party.add(arrived)

guests_who_did_not_come = sorted(reservation_codes - arrived_to_the_party)

print(len(guests_who_did_not_come))
print("\n".join(guests_who_did_not_come))

