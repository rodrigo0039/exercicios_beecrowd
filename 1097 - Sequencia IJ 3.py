n = 7
for i in range(1, 9 + 1, 2):
    for j in range(7, 4, - 1):
        print(f"I={i} J={n}")
        n -= 1
    n += j