def d_c(x, y):
    if x > y:
        return print("Decrescente")
    return print("Crescente")


while True:
    x, y = map(int, input().split())
    if x == y:
        break
    d_c(x, y)