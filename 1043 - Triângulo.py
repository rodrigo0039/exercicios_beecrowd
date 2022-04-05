a1, a2, a3 = [float(x) for x in input().split()]
perimetro = 0
area = 0
if a1 < a2 + a3 and a1 + a2 > a3 and a1 + a3 > a2:
    perimetro = a1 + a2 + a3
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = (a1 + a2) * a3 / 2
    print(f'Area = {area:.1f}')