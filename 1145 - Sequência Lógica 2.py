c, ate = map(int, input().split())
x = 1
while x < ate:
    for i in range(c):
        if i == c - 1:
            print(x)
            x += 1
        elif x < ate:
            print(x, end=" ")
            x += 1