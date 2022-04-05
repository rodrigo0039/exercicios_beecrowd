intervalo = []
cont_sim = 0
cont_nao = 0
for x in range(10, 20, 1):
    intervalo.append(x)
for i in range(int(input())):
    numero = int(input())
    if numero in intervalo:
        cont_sim += 1
    else:
        cont_nao += 1
print(f"{cont_sim} in\n{cont_nao} out")