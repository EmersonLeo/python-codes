'''

Link do desafio: http://olimpiada.ic.unicamp.br/pratique/programacao/nivel1/2007f1p1_perdida

@author: emersonleo

'''

a= input().split(" ")
h=[]
for i in a:
    b=int(i)
    h.append(b)
h.remove(h[0])
h.sort()


def lost(lista):
    L1=[]
    a=0
    for i in range(1,len(lista)+2):
        L1.append(i)
        k=0
        y=0


    for i in range(1,len(L1)):
        if L1[k] == lista[y]:
            k+=1
            y+=1
            continue
    else:
        print(L1[k])








p=lost(h)
