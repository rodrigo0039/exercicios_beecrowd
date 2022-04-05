while True:
    x = list(range(1, int(input()) + 1))
    if len(x) == 0:
        break
    print(*x, sep=" ")