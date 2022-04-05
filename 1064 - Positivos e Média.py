positivos = 0
soma = 0

for x in range(6):
    n = float(input())
    if n > 0.0:
        positivos = positivos + 1
        soma = soma + n
print(f'{positivos} valores positivos\n{soma/positivos:.1f}')