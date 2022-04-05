num = input() .split()
A = float(num[0])
B = float(num[1])
C = float(num[2])
pi = 3.14159

triangulo = A * C / 2
circulo = pi * C**2
trapezio = (A + B) * C / 2
quadrado = B * B
retangulo = A * B
print(f'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\n')