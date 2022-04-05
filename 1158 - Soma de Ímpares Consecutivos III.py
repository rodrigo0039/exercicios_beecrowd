for i in range(int(input())):
    x, y = map(int, input().split())
    soma_impar = 0
    cont = 0
    while cont != y:
        if x % 2 == 1:
            soma_impar += x
            cont += 1
        x += 1
    print(soma_impar)