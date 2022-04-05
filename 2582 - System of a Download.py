Nmusicas = int(input())
album = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!',
         'CRIPTONIZE','OFFLINE DAY', 'SALT', 'ANSWER!','RAR?',
         'WIFI ANTENNAS']
somabotao = []
for x in range(Nmusicas):
  botao1, botao2 = [int(x) for x in input().split()]
  somabotao.append(botao1 + botao2)

for x in range(Nmusicas):
  print(album[somabotao[x]])
