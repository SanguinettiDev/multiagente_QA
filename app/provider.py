import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# --- MUDANÇA AQUI: Não iniciamos o cliente logo de cara ---
client = None 
modelo = os.getenv("model", "gpt-4o-mini")

def get_openai_client():
    """Garante que o cliente só é criado na hora do uso"""
    global client
    if client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            # Isso evita que o servidor caia, apenas retorna erro na requisição
            raise ValueError("A chave OPENAI_API_KEY não foi configurada no ambiente!")
        client = OpenAI(api_key=api_key)
    return client

def chamar_openai(system_prompt: str, user_prompt: str):
    try:
        # Chamamos a função que cria o cliente agora
        meu_cliente = get_openai_client()
        
        response = meu_cliente.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na chamada OpenAI: {str(e)}"