while True:
    teste = int(input())
    if teste == 0:
        break
    n, m = map(int, input().split())
    for j in range(teste):
        x, y = map(int, input().split())
        if x > n and y > m:
            print("NE")
        elif x == n or y == m:
            print("divisa")
        elif x < n and y > m:
            print("NO")
        elif x > n and y < m:
            print("SE")
        else:
            print("SO")