n = int(input())
vetor = []
count = 0
for i in range(1000):
    vetor.append(count)
    print(f"N[{i}] = {vetor[i]}")
    count += 1
    if count == n:
        count = 0