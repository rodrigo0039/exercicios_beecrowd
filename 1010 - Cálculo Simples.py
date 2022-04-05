listapecaum = input() .split()

codp = int(listapecaum[0])
qntp = int(listapecaum[1])
vp = float(listapecaum[2])
x = qntp * vp

listapeca2 = input() .split()

codp2 = int(listapeca2[0])
qntp2 = int(listapeca2[1])
vp2 = float(listapeca2[2])
x2 = qntp2 * vp2

X = x + x2
print(f'VALOR A PAGAR: R$ {X:.2f}')