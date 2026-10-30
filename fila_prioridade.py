# fila_prioridade.py
# Fila de prioridade com três filas encadeadas: ALTA, MÉDIA e BAIXA.
# O atendimento começa sempre pela ALTA e, dentro de cada nível, segue a ordem de chegada.

from fila import FilaEncadeada


class Chamado:
    # Um chamado de suporte: o texto e a urgência classificada pela IA

    def __init__(self, texto, urgencia):
        self.texto = texto
        self.urgencia = urgencia


class FilaPrioridade:
    def __init__(self):
        self.alta = FilaEncadeada()
        self.media = FilaEncadeada()
        self.baixa = FilaEncadeada()

    def inserir(self, texto, urgencia):
        # Coloca o chamado na fila do seu nível de urgência

        chamado = Chamado(texto, urgencia)
        if urgencia == "ALTA":
            self.alta.enqueue(chamado)
        elif urgencia == "MÉDIA":
            self.media.enqueue(chamado)
        else:
            self.baixa.enqueue(chamado)

    def atender(self):
        # Devolve o próximo chamado: ALTA primeiro, depois MÉDIA, depois BAIXA.

        if not self.alta.esta_vazia():
            return self.alta.dequeue()
        if not self.media.esta_vazia():
            return self.media.dequeue()
        return self.baixa.dequeue()   # Se estiver vazia, devolve None

    def listar(self):
        # Mostra os chamados na ordem em que serão atendidos

        if self.alta.esta_vazia() and self.media.esta_vazia() and self.baixa.esta_vazia():
            print("Nenhum chamado na fila.")   # Se as três filas estiverem vazias, avisa o usuário
        else:
            mostrar(self.alta)
            mostrar(self.media)
            mostrar(self.baixa)


def mostrar(fila):
    # Percorre os nós de uma fila, do início ao fim, e imprime cada chamado

    atual = fila.inicio
    while atual is not None:
        print(f"[{atual.dado.urgencia}] {atual.dado.texto}")
        atual = atual.proximo