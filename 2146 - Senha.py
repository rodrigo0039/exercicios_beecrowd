while True:
    try:
        senha = int(input())
        senha = senha - 1
        print(senha)
    except:
        EOFError
        break