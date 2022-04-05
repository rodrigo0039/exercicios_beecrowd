g = 0
v_inter = 0
v_gremio = 0
e = 0

while True:
    inter, gremio = map(int, input().split())
    if inter > gremio:
        v_inter += 1
    else:
        v_gremio += 1
    if inter == gremio:
        e += 1
    g += 1
    p = int(input("Novo grenal (1-sim 2-nao)\n"))
    if p != 1:
        break
print(f"{g} grenais\nInter:{v_inter}\nGremio:{v_gremio}\nEmpates:{e}")
if v_inter > v_gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais ")