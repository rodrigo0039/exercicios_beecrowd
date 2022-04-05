teste = int(input())
for i in range(teste):
    pa, pb, g1, g2 = map(float, input().split())
    cont = 0
    while pa <= pb:
        pa += (pa * g1) // 100
        pb += (pb * g2) // 100
        cont += 1
        if cont > 100:
            break
    if cont == 101:
        print("Mais de 1 seculo.")
    else:
        print(f"{cont} anos.")