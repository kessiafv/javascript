import random #importar o módulo random para embaralhar as cartas

def embaralhaCartas(baralho):
    #embaralhar o baralho usando a função shuffle da bibliotecha random
    random.shuffle(baralho)

    #retorna o baralho embaralhado com uma pilha de cartas
    return baralho

def compraCartas(pilhaCartas):
    #verifica se ainda há cartas na pilha
    if len(pilhaCartas) > 0:
        #remove a carta do topo da pilha
        carta_comprada = pilhaCartas.pop()
        #imprime a carta comprada
        print("Comprou a carta:", carta_comprada)
    else:
        print("A pilha de cartas está vazia!")

#testar as funções
baralho = ['A-Paus', '2-Paus', '3-Paus', '4-Paus', '5-Paus', '6-Paus', '7-Paus', '8-Paus', '9-Paus', '10-Paus', 'J-Paus', 'Q-Paus', 'K-Paus', 'A-Copas', '2-Copas', '3-Copas', '4-Copas', '5-Copas', '6-Copas', '7-Copas', '8-Copas', '9-Copas', '10-Copas', 'J-Copas', 'Q-Copas', 'K-Copas', 'A-Ouros', '2-Ouros', '3-Ouros', '4-Ouros', '5-Ouros', '6-Ouros', '7-Ouros', '8-Ouros', '9-Ouros', '10-Ouros', 'J-Ouros', 'Q-Ouros', 'K-Ouros', 'A-Espadas', '2-Espadas', '3-Espadas', '4-Espadas', '5-Espadas', '6-Espadas', '7-Espadas', '8-Espadas', '9-Espadas', '10-Espadas', 'J-Espadas', 'Q-Espadas', 'K-Espadas']

#embaralha o baralho e recebe a pilha de cartas
pilhaCartas = embaralhaCartas(baralho)

#compra e imprime a primeira carta
compraCartas(pilhaCartas)

#compra e imprime a segunda carta
compraCartas(pilhaCartas)

#compra e imprime a terceira carta
compraCartas(pilhaCartas)
