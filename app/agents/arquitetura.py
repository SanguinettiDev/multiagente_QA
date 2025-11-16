from crewai import Agent, Task
from app.provider import get_llm

def criar_agente_arquitetura():
    return Agent(
        role='Arquiteto de Software',
        goal='Definir a stack tecnológica, estrutura de pastas e padrões de projeto baseados no backlog.',
        backstory="Você desenha soluções escaláveis. Você decide quais bibliotecas, banco de dados e padrões (MVC, Clean Arch) usar.",
        llm=get_llm(),
        verbose=True
    )

def tarefa_arquitetura(agente, contexto_backlog):
    return Task(
        description="Com base no Backlog gerado, defina a Arquitetura Técnica, Stack (Frontend/Backend) e Estrutura de Pastas.",
        expected_output="Documento de Arquitetura Técnica e Árvore de Arquivos.",
        agent=agente,
        context=[contexto_backlog]
    )