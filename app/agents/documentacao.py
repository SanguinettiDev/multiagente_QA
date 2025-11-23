from app.provider import chamar_openai

def executar_docs(arquitetura_gerada):
    system_prompt = (
        "Você é um Tech Writer especialista.\n"
        "Sua função é escrever a documentação técnica e um README.md perfeito.\n"
        "Inclua como instalar, rodar e a estrutura do projeto."
    )
    
    user_prompt = (
        f"Escreva o conteúdo de um arquivo README.md baseado nesta arquitetura:\n\n"
        f"{arquitetura_gerada}"
    )
    
    print("--- [TECH WRITER] Escrevendo Docs... ---")
    return chamar_openai(system_prompt, user_prompt)