import os
from dotenv import load_dotenv
from crewai import LLM

# Carrega o .env explicitamente
load_dotenv()

def get_llm():
    """Retorna a instância do LLM configurada."""
    api_key = os.getenv("OPENAI_API_KEY")
    # Se não tiver 'model' no .env, usa gpt-4-turbo por padrão
    model = os.getenv("model", "gpt-4-turbo")
    
    if not api_key:
        # Isso vai te ajudar a descobrir se o .env está sendo lido errado
        raise ValueError("ERRO CRÍTICO: A variável OPENAI_API_KEY não foi encontrada. Verifique seu arquivo .env")

    return LLM(model=model, api_key=api_key)