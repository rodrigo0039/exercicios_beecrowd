par = []
impar = []
cont_par = 0
cont_impar = 0
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        cont_par += 1
        if cont_par == 5:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par.clear()
    else:
        impar.append(n)
        cont_impar += 1
        if cont_impar == 5:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar.clear()
if len(impar) != 0:
    for i in range(len(impar)):
        print(f"impar[{i}] = {impar[i]}")
if len(par) != 0:
    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")