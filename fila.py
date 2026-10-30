# fila.py
# Fila (FIFO) feita do zero, com nós e ponteiros.
# Primeiro a entrar, primeiro a sair. Não usa list, queue nem deque.

class No:
    # Guarda um dado e aponta para o próximo nó

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None   # None = não há próximo (é o último)


class FilaEncadeada:
    def __init__(self):
        self.inicio = None   # primeiro nó: o próximo a sair
        self.fim = None      # último nó: onde entram os novos

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, dado):
        # Coloca um dado no fim da fila

        novo = No(dado)
        if self.esta_vazia():
            self.inicio = novo            # fila vazia: o novo é o primeiro e o último
            self.fim = novo
        else:
            self.fim.proximo = novo       # o último atual aponta para o novo
            self.fim = novo               # o novo passa a ser o último

    def dequeue(self):
        # Tira e devolve o dado do início da fila (ou None se estiver vazia)

        if self.esta_vazia():
            return None
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo   # o segundo nó vira o primeiro
        if self.inicio is None:             # a fila esvaziou:
            self.fim = None                 # o fim também não aponta mais para ninguém
        return dado