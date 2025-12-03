from app.provider import chamar_openai

def executar_docs(casos_teste):
    system_prompt = (
        "Você é um QA Automation Engineer (SDET)\n"
        "Sua função é transformar casos de teste em CÓDIGO executável.\n"
        "Gere scripts de teste que validem os cenários propostos."
    )
    
    user_prompt = (
        f"Gere um script na linguagem dita utilizando a bibliotecas necessarias para cobrir estes cenários:\n\n"
        f"{casos_teste}\n\n"
        f"REGRAS:\n"
        f"- O código deve ser copiável e executável.\n"
        f"- Use Mocks se necessário.\n"
        f"- Adicione comentários explicando o que cada teste valida."
    )
    
    print("--- [QA AUTOMATION] Gerando scripts Python... ---")
    return chamar_openai(system_prompt, user_prompt)