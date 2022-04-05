cont = 0
m = 0
p = 0
while True:
    nota = float(input())
    if 0 <= nota <= 10:
        m += nota
        cont += 1
    else:
        print("nota invalida")
    if cont == 2:
        print(f"media = {m / 2:.2f}")
        cont = 0
        m = 0
        while True:
            p = int(input("novo calculo (1-sim 2-nao)\n"))
            if p == 1 or p == 2:
                break
        if p == 2:
            break