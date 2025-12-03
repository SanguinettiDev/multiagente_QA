from app.provider import chamar_openai

def executar_arquitetura(estrategia_qa):
    system_prompt = (
        "Você é um QA Analyst especialista em BDD (Behavior Driven Development).\n"
        "Sua função é criar Casos de Teste detalhados baseados na estratégia fornecida.\n"
        "Cubra caminhos felizes (Happy Path) e caminhos de erro (Sad Path)."
    )
    
    user_prompt = (
        f"Com base nesta Estratégia de QA, escreva os Cenários de Teste:\n\n"
        f"{estrategia_qa}\n\n"
        f"SAÍDA ESPERADA:\n"
        f"- Use formato Gherkin (Dado / Quando / Então) onde possível.\n"
        f"- Crie pelo menos 3 cenários de sucesso e 3 de erro/exceção.\n"
        f"- Seja extremamente detalhista nos dados de entrada."
    )
    
    print("--- [QA DESIGN] Escrevendo casos de teste (Gherkin)... ---")
    return chamar_openai(system_prompt, user_prompt)