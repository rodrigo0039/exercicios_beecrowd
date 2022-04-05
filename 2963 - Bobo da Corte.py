n = int(input())
votos = []

i = 0
while ( i < n ):
  votos.append(int(input()))
  i = i + 1

vmax = max(votos)

if (votos[0] == vmax) :
  print('S')
else:
  print('N')