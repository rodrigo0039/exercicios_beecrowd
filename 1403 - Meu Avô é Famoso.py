while True:
    ranking, jogador = [int(x) for x in input().strip().split(" ")]
    if ranking == 0 and jogador == 0:
        break
    lista = []
    for i in range(ranking):
        lista.extend(int(j) for j in input().split())
    lista.sort()
    cont = 1
    lista_cont = {}
    tam = len(lista)
    for i in range(0, tam):
        ant = lista[i]
        if i == tam - 1:
            lista_cont[ant] = cont
            break
        prox = lista[i + 1]
        if ant == prox:
            cont += 1
        else:
            lista_cont[ant] = cont
            cont = 1
    seg = 0
    maximo = max(lista_cont.values())
    minimo = min(lista_cont.values())
    for i in lista_cont.values():
        if maximo > i > seg:
            seg = i
    for k, v in lista_cont.items():
        if v == seg:
            print(k, end=" ")
    print()