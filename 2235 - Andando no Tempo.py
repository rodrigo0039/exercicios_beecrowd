entrada = input().split( )

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

if(a==b or b==c or a==c or a == b + c or b == a + c or c == a + b):
  print('S')
else :
  print('N')