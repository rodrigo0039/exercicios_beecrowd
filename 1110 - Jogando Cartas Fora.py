from collections import deque
while True:
    numero = int(input())
    if numero == 0:
        break
    cartas = deque(range(1, numero + 1))
    removidos = []
    while len(cartas) != 1:
        removidos.append(cartas.popleft())
        cartas.append(cartas.popleft())
    print("Discarded cards:", str(removidos).replace("[", "").replace("]", ""))
    print(f"Remaining card: {cartas[0]}")