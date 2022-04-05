impar = []
par = []
positos = []
negativos = []
for i in range(5):
    n = int(input())
    if n >= 0:
        if n == 0:
            par.append(n)
            continue
        positos.append(n)
    else:
        negativos.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f"{len(par)} valor(es) par(es)")
print(f"{len(impar)} valor(es) impar(es)")
print(f"{len(positos)} valor(es) positivo(s)")
print(f"{len(negativos)} valor(es) negativo(s)")

