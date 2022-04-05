dia_i = int(input().split()[1])
hora_inicial, min_inicial , s_inicial = [int(x) for x in input().split(":")]

dia_f = int(input().split()[1])
hora_final, min_final, s_final = [int(x) for x in input().split(":")]

e1 = s_inicial + min_inicial * 60 + hora_inicial * 3600 + dia_i * 24 * 3600
e2 = s_final + min_final * 60 + hora_final * 3600 + dia_f * 24 * 3600
tempo = e2 - e1

dia = tempo // (24 * 3600)
print(f"{dia} dia(s)")
tempo %= (24 * 3600)
hora = tempo // 3600
print(f"{hora} hora(s)")
tempo %= 3600
minuto = tempo // 60
print(f"{minuto} minuto(s)")
tempo %= 60
segundos = tempo
print(f"{segundos} segundo(s)")