i = int(0)
cont = 0
while i <= 2.1:
    j = 1
    while j <= 3:
        k = i + j
        if i == 0 or i > 1.8 or i > 0.9 and i < 1.1:
            print(f"I={round(i)} J={int(k)}")
        else:
            print(f"I={i:.1f} J={k:.1f}")
        j+= 1
    i+= 0.2
