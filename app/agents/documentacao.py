from crewai import Agent, Task
from app.provider import get_llm

def criar_agente_docs():
    return Agent(
        role='Tech Writer',
        goal='Escrever a documentação técnica e o README.md do projeto.',
        backstory="Você garante que o projeto seja compreensível. Você escreve READMEs perfeitos e guias de instalação.",
        llm=get_llm(),
        verbose=True
    )

def tarefa_docs(agente, contexto_arquitetura):
    return Task(
        description="Escreva um README.md completo e documentação da API baseada na arquitetura definida.",
        expected_output="Conteúdo Markdown do README.md.",
        agent=agente,
        context=[contexto_arquitetura]
    )