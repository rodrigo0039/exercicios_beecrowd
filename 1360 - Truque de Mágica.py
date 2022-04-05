def retorna(z1, z2, z3):
    if z1 < z2 < z3:
        return 1
    if z1 < z3 < z2:
        return 2
    if z2 < z1 < z3:
        return 3
    if z3 < z1 < z2:
        return 4
    if z2 < z3 < z1:
        return 5
    else:
        return 6


naipes = {"H": 10, "C": 30, "D": 50, "S": 90}
cartas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
especiais = {"T": 10, "J": 11, "Q": 12, "K": 13}

for _ in range(int(input())):
    lista_cartas = list(map(str, input().split()))
    n_valor = [0] * 4
    for i in range(4):
        n_valor[i] = lista_cartas[i][0]
        if n_valor[i] in especiais:
            n_valor[i] = especiais.get(lista_cartas[i][0])
        else:
            n_valor[i] = int(n_valor[i])

    n_naipes = []

    for j in range(0, 3):
        n_naipes.append(lista_cartas[j + 1][1])
        if n_naipes[j] in naipes:
            n_naipes[j] = naipes.get(lista_cartas[j + 1][1])
        else:
            n_naipes[j] = int(n_naipes[j])

    cartas_atuais = [0] * 3
    for x in range(3):
        cartas_atuais[x] = n_valor[x + 1] + n_naipes[x]
    z1 = cartas_atuais[0]
    z2 = cartas_atuais[1]
    z3 = cartas_atuais[2]
    pos = n_valor[0] + retorna(z1, z2, z3)
    if pos > 13:
        pos -= 13
    carta_final = cartas[pos - 1]

    print(f"{carta_final}{lista_cartas[0][1]}")