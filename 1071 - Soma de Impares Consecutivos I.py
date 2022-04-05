numero = []
total = 0
for i in range(2):
    numero.append(int(input()))
for x in range(numero[0] - 1, numero[1], -1):
    if x % 2 == 1:
        total += x
print(total)