n1, n2, n3 = [int(x) for x in input().split()]
a1 = n1
a2 = n2
a3 = n3
aux = 0
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
elif n1 > n3:
    aux = n1
    n1 = n3
    n3 = aux
if n2 > n3:
    aux = n2
    n2 = n3
    n3 = aux
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
print(f'{n1}\n{n2}\n{n3}\n\n{a1}\n{a2}\n{a3}')