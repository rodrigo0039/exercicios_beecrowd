def j(n, k):
    res = 0
    for i in range(1, n + 1):
        res = (res + k) % i
    return res + 1


for i in range(int(input())):
    n, k = map(int, input().split())
    print(f"Case {i + 1}: {j(n, k)}")