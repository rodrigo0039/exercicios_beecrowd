def senha(x):
    if x == "2002":
        return print("Acesso Permitido")
    return print("Senha Invalida")


while True:
    x = input()
    senha(x)
    if x == "2002":
        break