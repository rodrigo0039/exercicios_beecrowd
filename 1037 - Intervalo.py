a = float(input())

if a <= 25 and a >= 0:
    print('Intervalo [0,25]')
if a > 25 and a <= 50:
    print('Intervalo (25,50]')
if a > 50 and a <= 75:
    print('Intervalo (50,75]')
if a > 75 and a <= 100:
    print('Intervalo (75,100]')
if a < 0 or a > 100:
    print('Fora de intervalo')