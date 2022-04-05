while True:
    g, p = map(int, input().split())
    if g == 0 or p == 0:
        break
    resultado = []
    chegada = []
    for i in range(g):
        chegada.append(list(map(int, input().split())))
    for x in range(len(chegada)):
        ordem = {}
        count = 1
        atual = chegada[x]
        for i in range(len(atual)):
            for j in range(len(atual)):
                if atual[j] == count and j + 1 not in ordem:
                    ordem[j + 1] = 0
                    count += 1
        resultado.append(ordem)
    s = int(input())
    for t in range(s):
        soma = {}
        l = 0
        corridas = list(map(int, input().split()))
        c = corridas[0]
        count = 1
        corridas.pop(0)
        for a in range(g):
            for c, k in enumerate(resultado[l]):
                if c == len(corridas):
                    break
                resultado[l][k] += corridas[c]
            l += 1
        for i in resultado:
            for k, v in i.items():
                if k not in soma.keys():
                    soma[k] = 0
                    soma[k] += v
                else:
                    soma[k] += v
        pontuacao_maxima = max(soma.values())
        pi = []
        for k, v in soma.items():
            if v == pontuacao_maxima:
                pi.append(k)
        for u in resultado:
            for k, v in u.items():
                u[k] = 0
        pi.sort()
        print(*pi, sep=" ")