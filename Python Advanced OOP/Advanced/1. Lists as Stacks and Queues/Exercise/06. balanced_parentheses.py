from _collections import deque

parentheses = deque(input())
opened_parentheses = deque()

while parentheses:

    left_par = parentheses.popleft()

    if left_par in "({[":
        opened_parentheses.append(left_par)

    elif not opened_parentheses:
        print("NO")
        break

    else:
        if f"{opened_parentheses.pop() + left_par}" not in "(){}[]":
            print("NO")
            break

else:
    print("YES")