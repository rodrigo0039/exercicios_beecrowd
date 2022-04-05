a1, a2, a3, a4 = [int(x) for x in input().split(' ')]
if a1 * a4 == a2 * a3:
    print('S')
elif a1 + a3 == a4 - a2:
    print('S')
else:
    print('N')