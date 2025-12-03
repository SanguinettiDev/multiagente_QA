from app.provider import chamar_openai

def executar_revisao(input_original, plano, automacao):
    system_prompt = (
        "Você é um Especialista em Segurança e Edge Cases (QA Security).\n"
        "Sua função é criticar o plano de testes atual e apontar falhas de segurança ou lógica extrema que foram esquecidas.\n"
        "Pense como um hacker ou um usuário mal-intencionado."
    )
    
    user_prompt = (
        f"INPUT ORIGINAL: {input_original}\n\n"
        f"PLANO ATUAL: {plano}\n"
        f"CÓDIGO GERADO: {automacao}\n\n"
        f"TAREFA:\n"
        f"1. Aponte vulnerabilidades de segurança (SQL Injection, XSS, Dados sensíveis) que não foram testadas.\n"
        f"2. Sugira 3 'Testes Destrutivos' para tentar quebrar o sistema.\n"
        f"3. Dê uma nota final (0-10) para a cobertura de testes."
    )
    
    print("--- [QA SECURITY] Procurando vulnerabilidades... ---")
    return chamar_openai(system_prompt, user_prompt)