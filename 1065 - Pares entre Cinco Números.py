contador = 0
for i in range(5):
    numeros = int(input())
    if numeros % 2 == 0:
        contador += 1
print(f"{contador} valores pares")