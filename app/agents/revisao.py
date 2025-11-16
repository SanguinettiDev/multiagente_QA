from crewai import Agent, Task
from app.provider import get_llm

def criar_agente_revisao():
    return Agent(
        role='QA Lead (Revisão)',
        goal='Criticar e validar se a arquitetura e o backlog atendem ao pedido original com qualidade.',
        backstory="Você é chato e detalhista. Você procura furos na lógica, problemas de segurança ou requisitos faltantes.",
        llm=get_llm(),
        verbose=True
    )

def tarefa_revisao(agente, input_original, tarefas_anteriores):
    return Task(
        description=f"Revise todo o trabalho (Backlog, Arq, Docs) frente ao pedido original: '{input_original}'. Dê uma nota 0-10 e liste melhorias.",
        expected_output="Relatório de Qualidade e Aprovação Final.",
        agent=agente,
        context=tarefas_anteriores
    )