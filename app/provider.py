import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Instancia o cliente uma vez só
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = os.getenv("model", "gpt-4o-mini")

def chamar_openai(system_prompt: str, user_prompt: str):
    """
    Função auxiliar que substitui o 'Agent' do CrewAI.
    Envia o System Prompt (quem é o agente) e o User Prompt (a tarefa).
    """
    try:
        response = client.chat.completions.create(
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