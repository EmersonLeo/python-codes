'''
@author: emersonleo

Disciplina: 06283 - Laboratório de Programação BSI 

Você e sua família acabaram de se mudar. Antes da mudança, você colocou um número na lateral de cada
um dos seus livros. Para facilitar a identificação dos livros, você fez uma lista, indicando o título
de cada livro e seu respectivo número, e guardou a lista dentro do livro de número 1. Chegando no seu
novo quarto, você viu que seus pais guardaram os livros em várias pilhas de livros, arrumadas em uma
fila de pilhas, com cada pilha encostada na pilha seguinte. Você é muito organizado e, por isso, antes
de abrir qualquer livro, você deseja recuperar a listagem. Por precaução, para evitar desabamentos, para
retirar o livro número um da pilha você precisa que ele esteja no topo da sua respectiva pilha e que as
duas pilhas vizinhas da atual estejam livres na altura desejada (isto é, não tenha nenhum livro adjacente).
Para isso, você precisa desempilhar alguns livros da pilha desejada e das suas pilhas vizinhas. Como o seu
quarto é bem grande, você sempre tem espaço para colocar os livros retirados em outro lugar, sem mexer nas
pilhas que os seus pais montaram. Para minimizar seu esforço, você deseja escrever um programa que, dadas
as posições dos livros nas pilhas, determine quantos livros precisa desempilhar para recuperar sua listagem.

Entrada: A única linha da entrada contém dois números inteiros N e P, indicando, respectivamente, o número
de livros e o número de pilhas (1 ≤ P ≤ N ≤ 1.000), separados por um espaço. Os livros são numerados
sequencialmente de 1 a N. Os números seguintes descrevem as pilhas. O início de cada pilha é indicado por
um traço. Os números, que são os identificadores dos livros, são separados por um espaço em branco.
Todas as pilhas contêm pelo menos um livro e todos os livros aparecem exatamente uma vez na entrada. Os
livros em cada pilha são listados em ordem, da base até o topo da pilha. Todos os livros têm o mesmo
formato.

Saída
Seu programa deve imprimir uma única linha, contendo um único inteiro: o número mínimo de livros, sem
contar o livro número 1, que você precisa desempilhar para recuperar a sua lista.

Exemplo de Entrada: 4 3 - 3 - 1 2 - 4

Exemplo de Saída: 3

'''

entrada = input().split()
entrada.append("-")
listaPilha = []
listaCompleta = []
listaT = [] 
saída = 0
E = 0
D = 0
P1 = 0
for i in range (3,len(entrada)):
    if (entrada[i]) != "-":
        listaPilha.append(entrada[i])
    else:
        listaCompleta.append(listaPilha)
        listaPilha = []
for livro in range(len(listaCompleta)):
    for j in range(len(listaCompleta[livro])):
        if listaCompleta[livro][j] == "1":
            pos1 = j
            if j == (len(listaCompleta[livro]) - 1):
                P1 = 0
                E = 0
                D = 0
                break
            else:
                P1 = len(listaCompleta[livro]) - (j + 1)
                if livro == 0:
                    E = 0
                else:
                    E = len(listaCompleta[livro - 1]) 
                if livro == (len(listaCompleta) - 1):
                    D = 0
                else:
                    D = len(listaCompleta[livro + 1]) 
saída = (E + D + P1) - pos1
if saída < 0:
  saída = 0
print(saída)
