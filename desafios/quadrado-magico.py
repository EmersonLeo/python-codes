'''

Link do desafio: http://olimpiada.ic.unicamp.br/pratique/programacao/nivel1/2007f1p1_magico

@author: emersonleo

'''

entrada = input().split()
numLC = int(entrada[0]) 
del(entrada[0])
numero = 0
cont = 0 
linha = [] 
listalinha = []
saída = 0
lista = []
for i in range(len(entrada)):
    if cont != numLC:
        numero += int(entrada[i])
        cont += 1
        lista.append(int(entrada[i]))
    else:
        listalinha.append(lista)
        linha.append(numero)
        lista = []
        numero = int(entrada[i])
        lista.append(numero)
        cont = 1
listalinha.append(lista)
linha.append(numero)
for j in range(len(linha)):
    if j < (len(linha) - 1):
        if linha[j] == linha[j+1]:
            saída = numero
        else:
            saída = -1
    else:
        break
valorColuna = 0
valorDiagonal = 0
cont2 = 0
for k in range (numLC):
    for l in range (numLC):
        valorColuna += listalinha[l][k]
        if (k == l) and (k + l) == (numLC - 1):
            valorDiagonal += (listalinha[l][k] * 2)
        elif (k == l) or (k + l) == (numLC - 1):
            valorDiagonal += listalinha[l][k]
        else:
            continue
cont2 = valorColuna//numLC
cont3 = valorDiagonal//2
if (cont2 and cont3) == numero:
    saida = numero
else:
    saída = -1
print(saída)
       
    
        

