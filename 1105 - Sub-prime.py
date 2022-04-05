cont = 0
while True:
    b, n = map(int, input().split())
    if b == 0 or n == 0:
        break
    creditos = list(map(int, input().split()))
    resultado = []
    for i in range(n):
        atual = list(map(int, input().split()))
        devedor = atual[0]
        credor = atual[1]
        creditos[devedor - 1] -= atual[-1]
        creditos[credor - 1] += atual[-1]
    if min(creditos) < 0:
        print("N")
    else:
        print("S")