from app.provider import chamar_openai

def executar_backlog(input_usuario):
    system_prompt = (
        "Você é um Product Owner (PO) experiente.\n"
        "Sua função é transformar ideias vagas em requisitos técnicos detalhados.\n"
        "Crie uma lista de Funcionalidades e User Stories com critérios de aceite."
    )
    
    user_prompt = f"Crie um Backlog detalhado para esta ideia: '{input_usuario}'"
    
    print("--- [PO] Gerando Backlog... ---")
    return chamar_openai(system_prompt, user_prompt)