'''
@author: emersonleo

Disciplina: 06283 - Laboratório de Programação BSI 

A coordenação do BSI está planejando uma semana de acolhimento aos novos alunos (semana da calourada), na qual,
dentre outras atividades, os estudantes participarão de diversos jogos legais para que fiquem conhecendo uns aos
outros em uma competição de times. Em uma das competições, todos os calouros aguardam em uma linha e então eles
deverão se reorganizar de acordo com algum critério, como por exemplo, a altura, data de nascimento, ou número de
matrícula/CPF. Esta reorganização da linha deverá ser realizada somente através de trocas sucessivas de pares de
estudantes.Deste modo, somente uma troca é realizada por vez para dois estudantes consecutivos. O time que terminar
mais rápido será o vencedor. Portanto, para que o time termine mais rapidamente, você deverá minimizar a quantidade
de trocas necessárias para atingir o objetivo.

Entrada: A única linha da entrada inicia por um número inteiro N (0 < N <= 1000000) indicando o número de estudantes
do time. Em seguida, serão informados N números dos estudantes (IDs), sendo que cada estudante só aparecerá uma única
vez. Todos os números serão separados por um espaço.
Saída: A saída deverá imprimir um número que indicará a quantidade mínima de trocas necessárias para organizar os
estudantes usando a ordem dos seus IDs.

ENTRADA:
3 3 1 2
SAÍDA:
2
'''

def bubble(lista,n):
    troca = True
    valor = 0
    while troca:
        troca = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                chave = lista[i]
                lista[i] = lista[i+1]
                lista[i + 1] = chave
                troca = True
                valor += 1
    return valor
entrada = ([int(x) for x in input().split()])
n = entrada[0]
entrada = entrada[1::]
print(bubble(entrada,n))
    
        
