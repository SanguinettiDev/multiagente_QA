import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from app.agents import backlog, arquitetura, documentacao, revisao

app = FastAPI()

class ProjectRequest(BaseModel):
    text: str

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "QA SQUAD AUTOMATION ONLINE. Envie o código/requisito para /generate"

@app.post("/generate", response_class=PlainTextResponse)
def run_agents(request: ProjectRequest):
    print(f"Recebendo demanda de QA: {request.text}")

    try:
        input_usuario = request.text
        
        # 1. Estratégia
        resultado_plano = backlog.executar_backlog(input_usuario)
        
        # 2. Casos de Teste
        resultado_casos = arquitetura.executar_arquitetura(resultado_plano)
        
        # 3. Script de Automação
        resultado_script = documentacao.executar_docs(resultado_casos)
        
        # 4. Análise de Segurança
        resultado_security = revisao.executar_revisao(
            input_usuario, 
            resultado_plano, 
            resultado_script
        )

        # Monta o Relatório
        relatorio = ""
        relatorio += "========================================\n"
        relatorio += "       RELATÓRIO DE QA & AUTOMAÇÃO      \n"
        relatorio += "========================================\n\n"

        relatorio += "### 1. ESTRATÉGIA DE TESTES ###\n"
        relatorio += str(resultado_plano) + "\n\n"
        relatorio += "----------------------------------------\n\n"

        relatorio += "### 2. CASOS DE TESTE (GHERKIN) ###\n"
        relatorio += str(resultado_casos) + "\n\n"
        relatorio += "----------------------------------------\n\n"

        relatorio += "### 3. SCRIPT DE AUTOMAÇÃO (PYTHON) ###\n"
        relatorio += str(resultado_script) + "\n\n"
        relatorio += "----------------------------------------\n\n"

        relatorio += "### 4. ANÁLISE DE SEGURANÇA & RISCOS ###\n"
        relatorio += str(resultado_security) + "\n\n"

        return relatorio

    except Exception as e:
        print(f"ERRO: {e}")
        return f"ERRO NO SERVIDOR: {str(e)}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)