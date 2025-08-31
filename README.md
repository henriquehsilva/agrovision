# 🌱 agrovision — FarmTech Solutions

Aplicação em Python para Agricultura Digital com:
- **2 culturas** (ex.: soja e café)
- **Cálculo de área** (retângulo para soja, círculo para café)
- **Manejo de insumos** (taxa por metro e por hectare)
- **Vetores** para organizar dados (lista de registros)
- **Menu** com entrada, saída, atualização, deleção e sair
- **Loops e decisões** no fluxo interativo
- **R** para estatística (média/desvio) e **clima** (API pública)
- **Testes** com `mamba + expects`
- **Docker** para padronizar o ambiente

## 🔧 Stack
Python 3.10+ · Typer · Rich · mamba · expects · R (r-base) · Docker

## 🗂 Estrutura
(ver pasta raiz do projeto)

## ▶️ Como rodar (local)
```bash
# 1) Ambiente
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install mamba expects

# 2) Executar menu
agrovision menu
