for i in range(int(input())):
    ano = 2015 - int(input())
    if ano < 0:
        print(f"{(ano - 1) * -1} A.C.")
    elif ano == 0:
        print(f"{ano + 1} A.C.")
    else:
        print(f"{ano} D.C.")