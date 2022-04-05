for i in range(int(input())):
    numero, letra, numero2 = [str(x) for x in input()]
    if numero != numero2:
        if letra == f"{letra.upper()}":
            print(f"{int(numero2) - int(numero)}")
        else:
            print(f"{int(numero2) + int(numero)}")
    else:
        print(f"{int(numero) * int(numero2)}")