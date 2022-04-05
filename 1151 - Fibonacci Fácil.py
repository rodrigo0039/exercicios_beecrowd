def fibo(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        if i == n - 1:
            print(n1)
        else:
            print(n1, end=" ")
            aux = n1
            n1 += n2
            n2 = aux


fibo(int(input()))