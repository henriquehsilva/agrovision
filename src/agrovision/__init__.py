"""
agrovision
Ferramentas para cálculo de área e manejo de insumos agrícolas.

Este pacote oferece a CLI (em `agrovision.cli:app`) e utilitários de domínio
para uso programático em outros módulos/scripts.
"""

from importlib import metadata as _metadata

# Versão do pacote (lida do pyproject quando instalado via pip).
try:
    __version__ = _metadata.version("agrovision")
except _metadata.PackageNotFoundError:  # execução local sem instalação
    __version__ = "0.0.0.dev0"

# Reexports úteis para uso direto: from agrovision import area_m2, ...
from .domain import (
    area_m2,
    insumo_litros_por_metro,
    insumo_por_hectare,
    Cultura,
    Geometria,
)

__all__ = [
    "__version__",
    "area_m2",
    "insumo_litros_por_metro",
    "insumo_por_hectare",
    "Cultura",
    "Geometria",
]
