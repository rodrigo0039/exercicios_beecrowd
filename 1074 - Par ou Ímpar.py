for i in range(int(input())):
    numero = int(input())
    if numero == 0:
        print("NULL")
        continue
    if numero > 0:
        if numero % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    else:
        if numero % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")