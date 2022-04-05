n = int(input())
vetor = list(map(int, input().split()))
menor = vetor[0]
posicao = 0
for i in range(1, len(vetor)):
    if menor > vetor[i]:
        menor, vetor[i] = vetor[i], menor
        posicao = i
print(f"Menor valor: {menor}\nPosicao: {posicao}")