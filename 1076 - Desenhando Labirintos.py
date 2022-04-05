teste = int(input())
for i in range(teste):
    matriz = [0] * 50
    for h in range(50):
        matriz[h] = [0] * 50

    inicio = int(input())
    contador = 0
    v, a = [int(x) for x in input().split(' ')]
    for j in range(a):
        u, c = [int(x) for x in input().split(' ')]
        if matriz[u][c] == 0:
            matriz[u][c] = 1
            matriz[c][u] = 1
            contador = contador + 2
    print(contador)