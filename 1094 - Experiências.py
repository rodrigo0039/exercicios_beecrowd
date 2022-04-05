t_c = 0
t_r = 0
t_s = 0
total = 0
for i in range(int(input())):
    numero, t = input().split()
    numero = int(numero)
    total += numero
    if t == "C":
        t_c += numero
    if t == "R":
        t_r += numero
    if t == "S":
        t_s += numero
print(f"Total: {total} cobaias\nTotal de coelhos: {t_c}\nTotal de ratos: {t_r}\nTotal de sapos: {t_s}\n"
      f"Percentual de coelhos: {(t_c * 100 / total):.2f} %\nPercentual de ratos: {(t_r * 100 / total):.2f} %\n"
      f"Percentual de sapos: {(t_s * 100/ total):.2f} %")