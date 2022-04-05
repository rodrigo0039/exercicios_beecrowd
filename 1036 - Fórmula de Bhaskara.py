import math
a, b, c = [float(x) for x in input().split(' ')]

delta = (b * b) - 4 * a * c
if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x = (-b + math.sqrt(delta)) / (2 * a)
    x1 = (- b - math.sqrt(delta)) / (2 * a)
    print(f'R1 = {x:.5f}\nR2 = {x1:.5f}')