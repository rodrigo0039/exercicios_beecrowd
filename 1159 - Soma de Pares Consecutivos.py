while True:
    x = int(input())
    if x == 0:
        break
    cont = 0
    soma_pares = 0
    while cont != 5:
        if x % 2 == 0:
            soma_pares += x
            cont += 1
        x += 1
    print(soma_pares)