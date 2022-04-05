n = float(input())
lista = []
lista.append(n)
print(f"N[{0}] = {lista[0]:.4f}")
for i in range(1, 100):
    lista.append(lista[i - 1] / 2)
    print(f"N[{i}] = {lista[i]:.4f}")