def tamanhoSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input())
for i in range(n):
    lista = input().split()
    tamanhoSort(lista)
    print(*lista, sep=" ")