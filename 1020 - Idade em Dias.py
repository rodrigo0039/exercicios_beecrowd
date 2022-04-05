a = int(input())
ano = a // 365
a = a % 365
mes = a // 30
dia = a % 30
print(f'{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)')