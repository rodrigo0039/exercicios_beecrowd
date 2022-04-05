while True:
    m = list(map(float, input().split()))
    if m[0] == 0:
        break
    print(f"{int((((m[0] * m[1]) * 100) / m[2]) ** 0.5)}")