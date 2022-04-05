valor = float(input())
valor = valor + 0.00001
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
resultado = 0

print('NOTAS:')
for x in range(6):
    print(f'{valor // notas[x]:.0f} nota(s) de R$ {notas[x]:.2f}')
    valor = valor % notas[x]
print('MOEDAS:')
for x in range(6):
    print(f'{valor // moedas[x]:.0f} moeda(s) de R$ {moedas[x]:.2f}')
    valor = valor % moedas[x]