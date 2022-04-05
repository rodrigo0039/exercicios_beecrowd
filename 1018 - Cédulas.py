valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for i in notas:
    qtd = valor// i
    print(f"{qtd} nota(s) de R$ {i},00")
    valor = valor % i