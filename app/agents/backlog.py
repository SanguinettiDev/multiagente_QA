from crewai import Agent, Task
from app.provider import get_llm

def criar_agente_backlog():
    return Agent(
        role='Product Owner (Backlog)',
        goal='Transformar uma ideia vaga em requisitos técnicos detalhados e User Stories.',
        backstory="Você é um PO experiente. Você detalha funcionalidades, critérios de aceite e regras de negócio.",
        llm=get_llm(),
        verbose=True
    )

def tarefa_backlog(agente, input_usuario):
    return Task(
        description=f"Analise a solicitação: '{input_usuario}'. Crie um Backlog detalhado com User Stories e Critérios de Aceite.",
        expected_output="Texto formatado com Lista de Funcionalidades e User Stories.",
        agent=agente
    )