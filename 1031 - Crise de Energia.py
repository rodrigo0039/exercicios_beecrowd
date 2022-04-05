def j(n, k):
    res = 0
    for i in range(1, n):
        res = (res + k) % i
    return res


while True:
    n = int(input())
    if n == 0:
        break
    k = 1
    while j(n, k) != 11:
        k += 1
    print(k)