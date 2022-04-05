n = int(input())

for i in range(1, n + 1):
    s = 1
    for j in range(3):
        s *= i
        if j == 2:
            print(s)
        else:
            print(s, end=" ")
    if i == n:
        break