binarios = []
g = 0
while True:
    if g == 3:
        break
    string = input()
    if string == "caw caw":
        print(sum(binarios))
        binarios.clear()
        g += 1
        continue
    string = string.replace("-", "0").replace("*", "1")
    b = int(string, 2)
    binarios.append(b)