from collections import deque

ramen_bowls = list(map(int, input().split(",")))
customers = deque(map(int, input().split(", ")))

while customers:
    if not ramen_bowls:
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break

    bowl = ramen_bowls.pop()
    person = customers.popleft()

    if bowl == person:
        continue

    elif bowl > person:
        ramen_bowls.append(bowl - person)

    else:
        customers.appendleft(person - bowl)

else:
    print("Great job! You served all the customers.")

    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen_bowls))}")