from math import pi
from typing import Literal, Dict, Any

Cultura = Literal["soja", "cafe"]
Geometria = Literal["retangulo", "circulo"]

def area_m2(cultura: Cultura, geometria: Geometria, params: Dict[str, float]) -> float:
    """
    Decisão do grupo (exemplo):
      - Soja  -> retângulo: largura_m * comprimento_m
      - Café  -> círculo  : pi * raio_m^2
    """
    if cultura == "soja" and geometria == "retangulo":
        return float(params["largura_m"]) * float(params["comprimento_m"])
    if cultura == "cafe" and geometria == "circulo":
        r = float(params["raio_m"])
        return pi * r * r
    raise ValueError("Combinação cultura/geometria ainda não suportada")

def insumo_litros_por_metro(taxa_ml_por_m: float, n_linhas: int, comprimento_linha_m: float) -> float:
    total_m = n_linhas * comprimento_linha_m
    return (taxa_ml_por_m * total_m) / 1000.0

def insumo_por_hectare(taxa_unid_por_ha: float, area_m2: float) -> float:
    # 1 ha = 10_000 m²
    return taxa_unid_por_ha * (area_m2 / 10_000.0)
