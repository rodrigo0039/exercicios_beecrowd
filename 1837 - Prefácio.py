a, b = map(int, input().split())
r = 0
t= 0
if a < 0:
    t = b
    f = 0
    if b < 0:
        t = b * -1
    while r < t:
        f = a - r
        if f % b == 0:
            break
        r += 1
    q = f / b
else:
    q = (a-(abs(a) % abs(b))) // b
    r = abs(a) % abs(b)

print(int(q), int(r))