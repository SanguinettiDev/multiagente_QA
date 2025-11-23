from app.provider import chamar_openai

def executar_revisao(ideia_original, backlog, arquitetura, docs):
    system_prompt = (
        "Você é um QA Lead (Revisor) extremamente crítico e detalhista.\n"
        "Sua função é validar se o que foi produzido atende ao pedido original.\n"
        "Procure falhas de lógica, segurança ou requisitos esquecidos."
    )
    
    user_prompt = (
        f"PEDIDO ORIGINAL: {ideia_original}\n\n"
        f"--- BACKLOG PRODUZIDO ---\n{backlog}\n\n"
        f"--- ARQUITETURA ---\n{arquitetura}\n\n"
        f"--- DOCUMENTAÇÃO ---\n{docs}\n\n"
        f"TAREFA: Dê uma nota 0-10, critique o trabalho da equipe e sugira melhorias finais."
    )
    
    print("--- [QA] Revisando tudo... ---")
    return chamar_openai(system_prompt, user_prompt)