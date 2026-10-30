# ia.py
# Integração com o Ollama (modelo llama3).
# Envia o texto do chamado e devolve a urgência: ALTA, MÉDIA ou BAIXA.

import ollama

MODELO = "llama3"   # pode trocar por "phi3"

PROMPT = (
    "Você é um sistema de triagem de chamados de suporte de TI.\n"
    "Classifique a urgência do chamado em exatamente uma palavra: ALTA, MEDIA ou BAIXA.\n"
    "- ALTA: sistema parado, perda de dados, segurança, muitos usuários afetados.\n"
    "- MEDIA: algo quebrado, lento ou instável que atrapalha o trabalho.\n"
    "- BAIXA: dúvida, pedido de melhoria ou problema estético.\n"
    "Responda SOMENTE com a palavra.\n\n"
    "Chamado: "
)


def classificar_urgencia(texto):
    # Devolve 'ALTA', 'MÉDIA' ou 'BAIXA'

    try:
        resposta = ollama.chat(
            model=MODELO,
            messages=[{"role": "user", "content": PROMPT + texto}],
            options={"temperature": 0},   # respostas mais estáveis
        )
    except Exception:
        # Se o Ollama estiver fechado, não perdemos o chamado: entra como MÉDIA.

        print("Aviso: não foi possível falar com o Ollama.")
        return "MÉDIA"

    conteudo = resposta["message"]["content"].upper()
    if "ALTA" in conteudo:
        return "ALTA"
    if "MEDIA" in conteudo or "MÉDIA" in conteudo:
        return "MÉDIA"
    if "BAIXA" in conteudo:
        return "BAIXA"
    return "MÉDIA"   # a IA respondeu algo inesperado
