import math
v1 = input() .split()
x1 = float(v1[0])
y1 = float(v1[1])
v2 = input() .split()
x2 = float(v2[0])
y2 = float(v2[1])
print(f'{math.sqrt((x1 - x2)**2 + (y1 - y2)**2):.4f}')