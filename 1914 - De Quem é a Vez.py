for i in range(int(input())):
    nomes = input().split()
    a, b = map(int, input().split())
    n1 = nomes[0]
    p1 = nomes[1]
    n2 = nomes[2]
    p2 = nomes[3]
    if p1 == "PAR":
        if (a + b) % 2 == 0:
            print(n1)
        else:
            print(n2)
    elif p1 == "IMPAR":
        if (a + b) % 2 == 1:
            print(n1)
        else:
            print(n2)