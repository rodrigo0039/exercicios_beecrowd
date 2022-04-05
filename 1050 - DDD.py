DDD = {'61': 'Brasilia', '71': 'Salvador', '11': 'Sao Paulo', '21': 'Rio de Janeiro',
       '32': 'Juiz de Fora', '19': 'Campinas', '27': 'Vitoria', '31': 'Belo Horizonte'}
numero = input()
if numero in DDD:
    print(DDD.get(numero))
else:
    print('DDD nao cadastrado')