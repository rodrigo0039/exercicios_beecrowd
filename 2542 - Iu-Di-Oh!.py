while True:
    try:
        Qatributo = int(input())
        m, l = [int(x) for x in input().split(' ')]
        cartas = []
        cartas_marcos = []
        cartas_leonardo = []
        for i in range(m):
            cartas = [int(e) for e in input().split()]
            cartas_marcos.append(cartas)
        for i in range(l):
            cartas = [int(e) for e in input().split()]
            cartas_leonardo.append(cartas)
        escolhaM, escolhaL = [int(x) for x in input().split()]
        atributo = int(input())
        if cartas_marcos[escolhaM - 1][atributo - 1] > cartas_leonardo[escolhaL - 1][atributo - 1]:
            print('Marcos')
        elif cartas_marcos[escolhaM - 1][atributo - 1] == cartas_leonardo[escolhaL - 1][atributo - 1]:
            print('Empate')
        else:
            print('Leonardo')
    except EOFError:
        break
