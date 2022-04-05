for i in range(int(input())):
    x , y = map(int, input().split())
    if x > y:
        x, y, = y, x
    soma = 0
    for j in range(x + 1, y):
        if j % 2 == 1:
            soma += j
    print(soma)