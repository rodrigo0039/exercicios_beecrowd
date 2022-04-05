vetor = [0] * 10
n = int(input())
for i in range(10):
    if i == 0:
        vetor[i] = n
    else:
        vetor[i] = vetor[i - 1] * 2
    print(f"N[{i}] = {vetor[i]}")