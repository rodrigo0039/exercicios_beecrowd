n1 = 0
n2 = 1
f = []
for i in range(64):
    f.append(n1)
    n1, n2 = n2, n1
    n1 += n2
n = int(input())
for i in range(n):
    numero = int(input())
    print(f"Fib({numero}) = {f[numero]}")
