from app.provider import chamar_openai

def executar_backlog(input_usuario):
    system_prompt = (
        "Você é um QA Manager Sênior.\n"
        "Sua função não é desenvolver, mas sim ANALISAR uma funcionalidade ou código pronto para criar uma ESTRATÉGIA DE TESTES.\n"
        "Identifique riscos, áreas críticas e tipos de testes necessários (Unitário, Integração, E2E, Carga)."
    )
    
    user_prompt = (
        f"Analise o seguinte input (Funcionalidade ou Código):\n"
        f"'{input_usuario}'\n\n"
        f"SAÍDA ESPERADA:\n"
        f"1. Resumo do que está sendo testado.\n"
        f"2. Lista de Funcionalidades Críticas.\n"
        f"3. Matriz de Riscos (Onde provavelmente vai quebrar?).\n"
        f"4. Estratégia recomendada (Ex: Focar 80% em testes de API e 20% em UI)."
    )
    
    print("--- [QA STRATEGY] Definindo plano de testes... ---")
    return chamar_openai(system_prompt, user_prompt)