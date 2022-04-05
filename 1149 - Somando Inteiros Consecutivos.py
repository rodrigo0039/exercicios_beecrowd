j = 1
lista = list(map(int, input().split()))
while True:
    a = lista[0]
    n = lista[j]
    if n > 0:
        break
    else:
        j += 1
soma = 0
for i in range(0, n):
    soma += (a + i)
print(soma)