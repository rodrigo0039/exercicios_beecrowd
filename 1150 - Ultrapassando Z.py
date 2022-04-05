x = int(input())
z = -999999
count = 1
while z <= x:
    z = int(input())
soma = x
while True:
    x += 1
    soma += x
    count += 1
    if soma > z:
        break
print(count)