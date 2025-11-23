from app.provider import chamar_openai

def executar_arquitetura(backlog_gerado):
    system_prompt = (
        "Você é um Arquiteto de Software Sênior.\n"
        "Sua função é definir a stack tecnológica, estrutura de pastas e padrões (MVC, Clean Arch).\n"
        "Você deve focar em escalabilidade e boas práticas."
    )
    
    user_prompt = (
        f"Com base neste Backlog, defina a Arquitetura Técnica, Banco de Dados e Estrutura de arquivos:\n\n"
        f"{backlog_gerado}"
    )
    
    print("--- [ARQUITETO] Desenhando Solução... ---")
    return chamar_openai(system_prompt, user_prompt)