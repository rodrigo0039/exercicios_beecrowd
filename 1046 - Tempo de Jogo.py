def tempod(x, y):
    if x > y:
        tempo = 24 - (x - y)
    elif y > x:
        tempo = y - x
    else:
        tempo = 24
    return tempo


inicio, final = [int(x) for x in input().split()]
print(f'O JOGO DUROU {tempod(inicio, final)} HORA(S)')
