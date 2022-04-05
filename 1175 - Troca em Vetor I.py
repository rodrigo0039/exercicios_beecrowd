vetor = [0] * 20

for i in range(len(vetor)):
    vetor[i] = int(input())
n = len(vetor) - 1
for j in range(len(vetor) // 2):
    vetor[j], vetor[n] = vetor[n], vetor[j]
    n -= 1
for x in range(20):
    print(f"N[{x}] = {vetor[x]}")