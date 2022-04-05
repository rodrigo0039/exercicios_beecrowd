def dfs(current, matrix, visited, count=2):
    if visited[current]:
        return
    visited[current] = 1
    for vizinhos in range(len(matrix)):
        if matrix[current][vizinhos] == 1:
            if visited[vizinhos] == 1:
                print(end=" " * count)
                print(f"{current}-{vizinhos}")
            else:
                print(end=" " * count)
                print(f"{current}-{vizinhos} pathR(G,{vizinhos})")
                dfs(vizinhos, matrix, visited, count + 2)


x = int(input())
for teste in range(x):
    print(f"Caso {teste + 1}:")
    v, a = map(int, input().split())
    matrix = [[0] * v for i in range(v)]
    visited = [0] * len(matrix)
    marcado = [0] * len(matrix)
    for i in range(a):
        p, d = map(int, input().split())
        marcado[p] = 1
        for j in range(a):
            if matrix[p][d] == 0:
                matrix[p][d] = 1
    for i in range(v):
        if visited[i] == 0 and marcado[i]:
            dfs(i, matrix, visited)
            print()