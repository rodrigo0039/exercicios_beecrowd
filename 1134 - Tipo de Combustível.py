a =0
g= 0
d= 0

while True:
    p = int(input())
    if 1 <= p <= 4:
        if p == 1:
            a += 1
        if p == 2:
            g += 1
        if p == 3:
            d += 1
        if p == 4:
            break
print(f"MUITO OBRIGADO\nAlcool: {a}\nGasolina: {g}\nDiesel: {d}")