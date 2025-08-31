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
# 1) Build da imagem
docker build -t agrovision .

# 2) inicialize os containers
docker compose up

# 3) inicializa do BD
printf "[]\n" > data/agrovision.json

# 4) Abrir o menu interativo
docker compose run --rm app agrovision menu

# 5) Abrir um shell no container
docker compose run --rm shell

# 6) Rodar testes (mamba)
docker compose run --rm test

# 7) Estatísticas em R (precisa do CSV exportado pelo menu antes)
docker compose run --rm r-stats

# 8) Clima em R (padrão LAT/LON do compose) 
docker compose run --rm r-clima

# ...ou sobrescrevendo coordenadas:
docker compose run --rm -e LAT=-22.90 -e LON=-47.06 r-clima
