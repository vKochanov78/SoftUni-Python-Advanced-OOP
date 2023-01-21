rows, cols = map(int, input().split())
s_e = ord("a")  # s_e => starting and ending ascii number

for r in range(s_e, s_e + rows):
    for c in range(s_e, s_e + cols):
        print(f'{chr(r)}{chr(r + c - s_e)}{chr(r)}', end=' ')
    print()