'''

@author: emersonleo

Disciplina: 06283 - Laboratório de Programação BSI
             
Um mercadinho lançou uma promoção imperdível: “Ganhe um refrigerante de brinde em troca de 3 vasilhames vazios”.
Você quer saber como obter a maior quantidade possível de brindes do mercadinho.

Entrada: A entrada possui vários casos, todos em uma única linha separados por um espaço, onde cada caso é
um número inteiro N (1 <= N <= 200).

Saída: Para cada caso de entrada, você terá que retornar a maior quantidade de refrigerantes que
conseguirá tomar2).Você pode pegar até 2 garrafas emprestadas mas deverá se certificar que terá esta quantidade
de garrafas vazias no final para devolver aos seus amigos. Todas as respostas devem estar na mesma linha,
separadas por espaços entre elas.

Exemplo de entrada:
8 5
Exemplo de saída:
12 7

'''
def comprar(valor):
    if valor == 0:
        return 0
    elif (valor > 0) and (valor%2) == 0:
        return comprar(valor -1 ) + 2
    else:
        return comprar(valor - 1) + 1
entrada = [int(x) for x in input().split()]
if len(entrada) == 1:
    print(comprar(entrada[0]))
else:
    print("%d %d" %(comprar(entrada[0]), comprar(entrada[1])))

