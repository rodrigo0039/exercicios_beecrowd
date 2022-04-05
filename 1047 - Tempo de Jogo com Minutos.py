hora_inicial, minuto_inicial, hora_final, minuto_final = [int(x) for x in input().split()]
hora = hora_final - hora_inicial
minuto = minuto_final - minuto_inicial
if minuto < 0:
    minuto += 60
    hora -= 1
if hora < 0:
    hora += 24
if hora == 0 and minuto == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')