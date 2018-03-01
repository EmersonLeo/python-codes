'''
Link do desafio: http://olimpiada.ic.unicamp.br/pratique/programacao/nivel1/2007f1p1_colisoes

Emerson Leonardo Oliveira de Lira

'''

def verInterseção(listaEntrada):
    lista = listaEntrada.split(" ")
    lista1 = []
    lista2 = []
    condição = True
    for elemento in range(len(lista)):
        if elemento <= 3:
            lista1.append(int(lista[elemento]))
        else:
            lista2.append(int(lista[elemento]))
    menor = min(lista2)
    cont = 0
    for elemento in lista2:
        if menor == elemento:
            break
        else:
            cont+= 1
    if (cont%2 != 0) and (cont != 0):
        condição = True
    else:
        if lista2[cont] >= lista2[cont + 1]:
            condição = True
        else:
            condição = False
    if (max(lista1) >= min(lista2)) and (condição == True):
        return 1
    else:
        return 0
a = input("")
print(verInterseção(a))
