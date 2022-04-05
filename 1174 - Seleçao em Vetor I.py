vetor = []

for i in range(100):
    vetor.append(float(input()))
    if vetor[i] <= 10:
        print(f"A[{i}] = {vetor[i]}")