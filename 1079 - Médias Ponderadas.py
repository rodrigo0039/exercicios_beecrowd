for i in range(int(input())):
    n1 , n2 , n3 = [float(x) for x in input().split()]
    media = (((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10 )
    print(f"{media:.1f}")