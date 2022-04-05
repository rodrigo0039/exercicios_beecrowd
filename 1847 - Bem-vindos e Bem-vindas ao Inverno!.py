a, b, c = map(int, input().split())

if a > b and b <= c or a < b < c and b - a <= c - b\
        or a > b > c and a - b > b - c or a == b and b < c:
    print(":)")
elif a < b and b >= c or a < b < c and b - a > c - b\
        or a > b > c and a - b < b - c or a == b and b > c:
    print(":(")
else:
    print(":(")
