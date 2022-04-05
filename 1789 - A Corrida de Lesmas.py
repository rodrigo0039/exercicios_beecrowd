while True:
    try:
        n = int(input())
        lesmas = list(map(int, input().split()))

        maior = max(lesmas)
        if maior < 10:
            print("1")
        elif 10 <= maior < 20:
            print("2")
        else:
            print("3")
    except EOFError:
        break