# Projeto 1 — Triagem Inteligente de Helpdesk

Estrutura de Dados I — Bacharelado em Sistemas de Informação

O usuário descreve um problema em texto. A IA (Ollama, modelo llama3) classifica a
urgência em **ALTA, MÉDIA ou BAIXA** e o chamado entra na fila de prioridade
correta. Ao atender, os chamados de prioridade ALTA saem primeiro.

## Arquivos

| Arquivo | O que faz |
|---|---|
| `fila.py` | `No` e `FilaEncadeada`: fila FIFO feita do zero, com ponteiros de início e fim (`enqueue`, `dequeue`) |
| `fila_prioridade.py` | `FilaPrioridade`: três filas (ALTA, MÉDIA, BAIXA). `inserir` escolhe a fila e `atender` esvazia ALTA, depois MÉDIA, depois BAIXA |
| `ia.py` | Envia o texto ao Ollama e devolve a urgência |
| `main.py` | Menu de terminal |

Nenhuma estrutura pronta do Python (`list.append()`, `queue.Queue`, `deque`) é usada
para guardar os chamados: tudo é feito com nós e ponteiros.

## Como rodar

1. Instale o [Ollama](https://ollama.com) e baixe o modelo:
   ```bash
   ollama pull llama3
   ```
2. Com o Ollama aberto, instale a biblioteca Python:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute:
   ```bash
   python main.py
   ```

## Exemplo

```
Opção: 1
Descreva o problema: O servidor da empresa caiu!
Chamado registrado como ALTA.

Opção: 2
Atendendo: [ALTA] O servidor da empresa caiu!
```
