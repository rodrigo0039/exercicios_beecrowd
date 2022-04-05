v1, v2, v3 = [float(x) for x in input().split()]
valores = list()
valores.extend([v1, v2, v3])
valores.sort(reverse=True)
if valores[0] >= valores[1] + valores[2]:
    print('NAO FORMA TRIANGULO')
else:
    if valores[0] * valores[0] == valores[1] * valores[1] + valores[2] * valores[2]:
        print('TRIANGULO RETANGULO')
    if valores[0] * valores[0] > valores[1] * valores[1] + valores[2] * valores[2]:
        print('TRIANGULO OBTUSANGULO')
    if valores[0] * valores[0] < ((valores[1] * valores[1]) + (valores[2] * valores[2])):
        print('TRIANGULO ACUTANGULO')
    if valores[0] == valores[1] and valores[0] == valores[2]:
        print('TRIANGULO EQUILATERO')
    if valores[1] == valores[2] and valores[0] != valores[1] or valores[0] == valores[1] and valores[2] != valores[1]:
        print('TRIANGULO ISOSCELES')
