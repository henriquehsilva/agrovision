FROM python:3.12-slim

# R para scripts
RUN apt-get update && apt-get install -y --no-install-recommends r-base && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip && pip install -e .

COPY src/ src/
COPY r/ r/
COPY specs/ specs/
RUN pip install mamba expects

# Diretórios de dados
RUN mkdir -p data exports

# Comandos úteis
# docker build -t agrovision .
# docker run -it --rm -v ${PWD}:/app agrovision bash
CMD ["bash"]
