resultado = 0
cont = 0
while True:
    i = int(input())
    if i < 0:
        break
    resultado += i
    cont += 1
print(f"{resultado/cont:.2f}")