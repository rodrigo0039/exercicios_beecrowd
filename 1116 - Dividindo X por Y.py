for i in range(int(input())):
    x , y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
        continue
    print(f"{x/y:.1f}")