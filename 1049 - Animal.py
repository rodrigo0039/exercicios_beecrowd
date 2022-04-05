opcoes = []

for i in range(3):
    opcoes.append(input())
if opcoes[0] == "vertebrado":
    if opcoes[1] == "ave":
        if opcoes[2] == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if opcoes[2] == "onivoro":
            print("homem")
        else:
            print("vaca")

if opcoes[0] == "invertebrado":
    if opcoes[1] == "inseto":
        if opcoes[2] == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if opcoes[2] == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")