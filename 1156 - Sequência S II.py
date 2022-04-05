i = 1
s = 1
soma = 0
while i <= 39:
    soma += i / s
    i += 2
    s *= 2
print(f"{soma:.2f}")