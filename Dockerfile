FROM python:3.12-slim

# R base + jsonlite
RUN apt-get update && apt-get install -y --no-install-recommends \
    r-base r-cran-jsonlite \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml ./
COPY src/ src/
COPY r/ r/
COPY specs/ specs/

RUN pip install --no-cache-dir --upgrade pip \
 && pip install -e . \
 && pip install mamba expects

RUN mkdir -p data exports
CMD ["bash"]
