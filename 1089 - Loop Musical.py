while True:
    try:
        n = int(input())
        contador = 0
        lista = [int(x) for x in input().split()]
        for i in range(1, n - 1):
            if lista[i] > lista[i - 1] and lista[i] > lista[i + 1] or lista[i] < lista[i - 1] and lista[i] < lista[i + 1]:
                contador += 1
        if lista[0] > lista[n - 1] and lista[0] > lista[1] or lista[0] < lista[n - 1] and lista[0] < lista[1]:
            contador += 1
        if lista[n - 1] > lista[n - 2] and lista[n - 1] > lista[0] or lista[n - 1] < lista[n - 2] and lista[n - 1] < lista[0]:
            contador += 1
        print(contador)
    except EOFError:
        break