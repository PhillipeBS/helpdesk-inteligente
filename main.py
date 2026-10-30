# main.py
# Menu de terminal do Helpdesk Inteligente.
# Registra chamados (a IA classifica a urgência), atende o próximo e lista a fila.
# Execute com: python main.py

from fila_prioridade import FilaPrioridade
from ia import classificar_urgencia


def main():
    fila = FilaPrioridade()

    while True:
        print("\n1) Registrar chamado")
        print("2) Atender próximo")
        print("3) Listar fila")
        print("0) Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            texto = input("Descreva o problema: ").strip()
            if texto != "":
                print("Classificando com a IA...")
                urgencia = classificar_urgencia(texto)
                fila.inserir(texto, urgencia)
                print(f"Chamado registrado como {urgencia}.")
        elif opcao == "2":
            chamado = fila.atender()
            if chamado is None:
                print("Nenhum chamado na fila.")
            else:
                print(f"Atendendo: [{chamado.urgencia}] {chamado.texto}")
        elif opcao == "3":
            fila.listar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


main()