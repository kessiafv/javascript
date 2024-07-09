class BST:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def inserir(self, dado):
        if self.dado == None:
            self.dado = dado
        else:
            if dado < self.dado:
                if self.esquerda:
                    self.esquerda.inserir(dado)
                else:
                    self.esquerda = BST(dado)
            else:
                if self.direita:
                    self.direita.inserir(dado)
                else:
                    self.direita = BST(dado)

    def folhas(self, lst):
        #verifica se o nó atual possui um dado válido
        if self.dado is not None:
            #se o nó atual for uma folha (não tem filhos) adiciona seu dado à lista
            if self.esquerda is None and self.direita is None:
                lst.append(self.dado)

            #verifica se há um filho à esquerda e, se houver, chama recursivamente a função para ele
            if self.esquerda:
                self.esquerda.folhas(lst)

            #verifica se há um filho à direita e, se houver, chama recursivamente a função para ele
            if self.direita:
                self.direita.folhas(lst)

        #retorna a lista atualizada contendo os dados dos nós folha
        return lst

# Teste
Teste = BST()
Teste.inserir(7)
Teste.inserir(4)
Teste.inserir(9)
Teste.inserir(0)
Teste.inserir(5)
Teste.inserir(8)
Teste.inserir(13)

print('Folhas: ', Teste.folhas([]))