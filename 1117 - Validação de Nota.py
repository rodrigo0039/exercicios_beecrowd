cont = 0
m = 0
while cont != 2:
    nota = float(input())
    if 0 <= nota <= 10:
        m += nota
        cont += 1
    else:
        print("nota invalida")
print(f"media = {m / 2:.2f}")