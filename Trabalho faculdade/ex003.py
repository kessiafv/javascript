class ElementoDaListaSimples:
    def __init__(self,dado,cor):
        self.dado = dado
        self.cor = cor
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None

    def inserirNoFinal(self, nodo):
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
        return

    def inserirPrioridade(self, nodo):
        # verificar se a lista está vazia
        if self.head is None:
            self.head = nodo # se estiver vazia, o nodo se torna o primeiro da lista
            return

        # caso a lista não esteja vazia
        nodo_atual = self.head
        nodo_anterior = None # mantém o rastreamento do nodo anterior

        # percorre a lista até encontrar o ponto de inserção
        while nodo_atual is not None and nodo_atual.cor == "A":
            nodo_anterior = nodo_atual #atualiza o nodo anterior
            nodo_atual = nodo_atual.proximo #move para o próximo nodo

        #se não tiver nenhum nodo com prioridade amarela na lista
        if nodo_anterior is None:
            nodo.proximo = self.head #o novo nodo se torna o primeiro da lista
            self.head = nodo
        else:
            #insere o novo nodo após o último nodo amarelo encontrado
            nodo_anterior.proximo = nodo
            nodo.proximo = nodo_atual
        return

    def inserir(self, dado, cor):
        nodo = ElementoDaListaSimples(dado, cor)
        if self.head is None:
            self.head = nodo
            return
        else:
            if nodo.cor == "V":
                self.inserirNoFinal(nodo)
            else:
                self.inserirPrioridade(nodo)
            return

#programa principal
filaPacientes = ListaEncadeadaSimples()

filaPacientes.inserir(1, "V") #insere um paciente com senha "V" 1
filaPacientes.inserir(2, "V") #insere um paciente com senha "V" 2
filaPacientes.inserir(101, "A") #insere um paciente com senha "A" 101
filaPacientes.inserir(3, "V") #insere um paciente com senha "V" 3
filaPacientes.inserir(102, "A") #insere um paciente com senha "A" 102
filaPacientes.inserir(103, "A") #insere um paciente com senha "A" 103
filaPacientes.inserir(4, "V") #insere um paciente com senha "V" 4
filaPacientes.inserir(104, "A") #insere um paciente com senha "A" 104
filaPacientes.inserir(105, "A") #insere um paciente com senha "A" 105

nodo_atual = filaPacientes.head
while nodo_atual is not None:
    print(f"Cartão: {nodo_atual.cor}, Senha: {nodo_atual.dado}")
    nodo_atual = nodo_atual.proximo

