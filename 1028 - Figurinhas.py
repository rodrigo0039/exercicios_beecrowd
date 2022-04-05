def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


teste = int(input())
for x in range(teste):
    num = input().strip().split(' ')
    print(mdc(int(num[0]), int(num[1])))