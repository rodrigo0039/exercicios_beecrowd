for i in range(int(input())):
    n = int(input())
    soma = 0
    for j in range(1, n):
        if n % j == 0:
            soma += j
    if soma == n:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")