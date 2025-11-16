import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew, Process
from fastapi.middleware.cors import CORSMiddleware

# Importa os módulos criados
from app.agents import backlog, arquitetura, documentacao, revisao

app = FastAPI()

# Configura CORS para aceitar seu Front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProjectRequest(BaseModel):
    idea: str

@app.post("/generate")
def run_agents(request: ProjectRequest):
    """Endpoint que roda a esteira de agentes"""
    input_usuario = request.idea
    
    # 1. Instancia Agentes
    agent_po = backlog.criar_agente_backlog()
    agent_arq = arquitetura.criar_agente_arquitetura()
    agent_doc = documentacao.criar_agente_docs()
    agent_qa = revisao.criar_agente_revisao()

    # 2. Cria Tarefas
    task_po = backlog.tarefa_backlog(agent_po, input_usuario)
    task_arq = arquitetura.tarefa_arquitetura(agent_arq, task_po)
    task_doc = documentacao.tarefa_docs(agent_doc, task_arq)
    task_qa = revisao.tarefa_revisao(agent_qa, input_usuario, [task_po, task_arq, task_doc])

    # 3. Monta a Equipe (Crew)
    factory_crew = Crew(
        agents=[agent_po, agent_arq, agent_doc, agent_qa],
        tasks=[task_po, task_arq, task_doc, task_qa],
        process=Process.sequential,
        verbose=True
    )

    # 4. Executa
    result = factory_crew.kickoff()
    
    return {"result": str(result)}

if __name__ == "__main__":
    import uvicorn
    # Roda o servidor
    uvicorn.run(app, host="0.0.0.0", port=8000)