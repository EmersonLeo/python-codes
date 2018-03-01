'''

@author: emersonleo

Disciplina: 06283 - Laboratório de Programação BSI 

O Diretório Acadêmico (DA) do BSI-UFRPE fez uma nova aquisição: uma mesa de ping-pong. Como a
demanda dos alunos é alta, eles devem formar equipes para participar do tênis de mesa. Cada
equipe possui 2 jogadores, portanto serão 4 pessoas jogando por vez. A ordem dos participantes
das partidas é definida através de uma fila, isto é, os 4 primeiros da fila irão jogar, em seguida
os outros 4, e assim por diante. Quem quiser jogar novamente deverá retornar para o fim da fila.
Para que as partidas sejam mais emocionantes, o D.A. decidiu que os quatro jogadores serão
distribuídos nas duas equipes de modo que as habilidades fiquem balanceadas. Cada jogador possui
um nível de habilidade que é representado por um número inteiro: quanto maior o número, melhor é o
jogador. A habilidade de uma equipe é medida como sendo a soma das habilidades dos seus
jogadores. Você deverá criar um algoritmo que deverá encontrar a menor distância possível entre os
níveis de habilidades dos 2 times.

Entrada: O arquivo de entrada consiste de quatro números inteiros dos jogadores da partida em uma
única linha separados por espaços. Cada número representa o nível de habilidade de um jogador.

Saída: A saída deve conter apenas uma linha com um número inteiro representando a menor diferença
possível entre os níveis de habilidade dos dois times.

'''

entrada = ([int(x) for x in input().split()])
cont = []
cont2 = 0
for elemento in range(len(entrada)):
  if elemento%2 == 1:
    cont2 = entrada[elemento] - entrada[elemento - 1]
    if cont2 < 0:
      cont2 = cont2*(-1)
      cont.append(cont2)
    else:
      cont.append(cont2)
print(max(cont) - min(cont))
    
    
  
