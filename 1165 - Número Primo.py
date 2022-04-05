def primo(numero):
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        print(f"{numero} eh primo")
    else:
        print(f"{numero} nao eh primo")


for i in range(int(input())):
    numero = int(input())
    primo(numero)