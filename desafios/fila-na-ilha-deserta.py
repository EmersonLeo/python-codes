'''
@author: emersonleo

Disciplina: 06283 - Laboratório de Programação BSI 

Considere que, em determinada ilha, todas as filas são formadas por ordem cronológica, isto é, as
pessoas mais idosas permanecem no início da fila, enquanto que as pessoas mais novas ficam no fim
da fila. Você deverá ordenar um conjunto de dados que conterá o nome e a idade das pessoas. Sua
ordenação deve levar em consideração somente a idade e, ao final, retornar uma lista de nomes
ordenados pela idade. Se houver empate, isto é, duas ou mais pessoas com a mesma idade, seu
algoritmo deverá deixá-las na ordem apresentada na entrada. Assim, uma pessoa que tiver chegado
primeiro à fila ficará na frente das outras de mesma idade que ela.

Entrada: A única linha da entrada possui vários pares “nome, idade” contendo o nome a idade das
pessoas na ordem em que chegaram na fila. As pessoas são separadas por vírgulas. Há 1000
habitantes na ilha, portanto este será o tamanho máximo possível da entrada.

Saída: A saída deverá exibir os nomes das pessoas ordenadas da mais idosa para a mais nova. Pessoas
de mesma idade devem ser ordenadas entre si usando a ordem de chegada. Os nomes devem ser separados
por vírgulas.

Exemplo de entrada:
Cicero, 30, Marcos, 40, Joao, 40, Adolfo, 40, Carlos, 13, Manoel, 60

Exemplo de saída:
Manoel, Marcos, Joao, Adolfo, Cicero, Carlos

'''

entrada = input().split(",")
dicNomes = {}
cont = 0
listaNome = []
listaNome2 = []
listaIdade = []
listaIdade2 = []
for i in entrada:
    if cont%2 == 0:
       dicNomes[(entrada[cont])] = int(entrada[cont + 1])
       listaIdade.append(int(entrada[cont + 1]))
       listaNome.append(entrada[cont])
       cont += 1
    else:
        cont += 1

for j in range(len(listaIdade)):
    maiorIdade = max(listaIdade)
    pos = listaIdade.index(maiorIdade)
    listaIdade[pos] = listaIdade[pos]*(-1)
    listaIdade2.append(maiorIdade)
for k in listaIdade2:
    pos = listaIdade.index(k*(-1))
    listaNome2.append(listaNome[pos]+",")
    del listaIdade[pos]
    del listaNome[pos]
listaNome2 = ''.join(listaNome2)
print(listaNome2[:-1])








    
    

        
