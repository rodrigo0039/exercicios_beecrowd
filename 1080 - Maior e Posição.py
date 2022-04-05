numeros= [0] * 100
maior = [[0,0]]
for i in range(100):
    numeros[i] = int(input())
    if numeros[i] > maior[0][0]:
        maior[0][0] = numeros[i]
        maior[0][1] = i + 1
print(f"{maior[0][0]}\n{maior[0][1]}")