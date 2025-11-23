import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Importamos as funções diretas
from app.agents import backlog, arquitetura, documentacao, revisao

app = FastAPI()

class ProjectRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "API Pure-Python (Sem CrewAI) Online."}

@app.post("/generate")
def run_agents(request: ProjectRequest):
    print(f"Recebendo pedido: {request.text}")

    try:
        input_usuario = request.text
        
        # 1. Executa Backlog (PO)
        resultado_backlog = backlog.executar_backlog(input_usuario)
        
        # 2. Executa Arquitetura (Passando o resultado do backlog)
        resultado_arq = arquitetura.executar_arquitetura(resultado_backlog)
        
        # 3. Executa Documentação (Passando o resultado da arquitetura)
        resultado_docs = documentacao.executar_docs(resultado_arq)
        
        # 4. Executa Revisão (Passando TUDO para o QA analisar)
        resultado_qa = revisao.executar_revisao(
            input_usuario, 
            resultado_backlog, 
            resultado_arq, 
            resultado_docs
        )

        # 5. Monta o Relatório Final Manualmente
        relatorio_completo = ""
        relatorio_completo += "=== 1. BACKLOG & USER STORIES ===\n"
        relatorio_completo += str(resultado_backlog) + "\n\n"
        
        relatorio_completo += "=== 2. ARQUITETURA TÉCNICA ===\n"
        relatorio_completo += str(resultado_arq) + "\n\n"
        
        relatorio_completo += "=== 3. DOCUMENTAÇÃO ===\n"
        relatorio_completo += str(resultado_docs) + "\n\n"
        
        relatorio_completo += "=== 4. REVISÃO DE QA ===\n"
        relatorio_completo += str(resultado_qa) + "\n\n"

        # Salva log local (opcional)
        try:
            nome_arquivo = f"projeto_clean_{input_usuario[:10].replace(' ', '_')}.md"
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(relatorio_completo)
        except:
            pass

        return {"result": relatorio_completo}

    except Exception as e:
        print(f"ERRO FATAL: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)