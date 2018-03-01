'''
@author: emersonleo

Disciplina: 06283 - Laboratório de Programação BSI 

Você deverá implementar um dicionário de palavras traduzidas para um idioma estrangeiro utilizando tabelas hash.
Seu trabalho será armazenar um conjunto de palavras e suas respectivas traduções. O dicionário pode ser
atualizado através de comandos para adição ou remoção de palavras. As consultas serão realizadas através de um
comando de busca. Os comandos de adição e remoção não produzem saídas pois somente alteram o estado interno da
tabela hash. O comando de busca gera saída com a respectiva palavra traduzida.

Entrada: O arquivo de entrada consiste de vários comandos em uma única linha separados por “;”. Os comandos
permitidos são:
• Operador de adição: A <palavra>:<tradução>;
• Operador de remoção: R <palavra>;
• Operador de busca: B <palavra>;
Podem aparecer palavras repetidas. Se isto ocorrer, você deverá armazenar a lista de traduções da palavra.
Se uma palavra com múltiplas traduções for removida, todas as traduções também serão apagadas. As
palavras/traduções podem conter hífen “-”.
Saída: A saída deve conter apenas os resultados do comando “B”. As saídas dos diversos comandos “B” devem
ser separadas por “;”. Se uma busca por uma palavra com múltiplas traduções for realizada, todas as
traduções deverão ser exibidas na saída separadas por “+:”. Se a palavra procurada não existir na tabela
hash, a saída deve ser “oxente?”.

Exemplo de Entrada:
A cachorro:dog;A gato:cat;A rato:mouse;A rato:rat;A informacao:information;A informacao:advice;B gato;R cachorro;B rato;B gato;
Exemplo de saída: Saída: dog;mouse+rat;oxente?;
'''
entrada = input().replace(";"," ").split(" ")
del entrada[-1]
dic = {}
listaPalavras = []
saída = " "
for elemento in range(len(entrada)):
    if elemento%2 == 0:
        if entrada[elemento] == "A":
            itemDic = entrada[elemento + 1].split(":")
            if itemDic[0] not in listaPalavras:
                dic[itemDic[0]] = []
                dic[itemDic[0]].append(itemDic[1])
                listaPalavras.append(itemDic[0])
            else:
                dic[itemDic[0]].append(itemDic[1])
        if entrada[elemento] == "R":
            listaPalavras.remove(entrada[elemento + 1])
        else:
            if entrada[elemento + 1] in listaPalavras:
                if len(dic[entrada[elemento + 1]]) > 1:
                    for palavra in dic[entrada[elemento + 1]]:
                        saída += palavra + "+"
                    saída = saída[1:(len(saída)-1)]
                    saída += ";"
                else:                    
                    add = dic[entrada[elemento + 1]]
                    saída += add[0] + ";"
            elif entrada[elemento] == "B":
                saída += "oxente?;"
print(saída)
            
    
            

