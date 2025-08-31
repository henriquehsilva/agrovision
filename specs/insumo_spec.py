# specs/area_spec.py
# -*- coding: utf-8 -*-
from mamba import description, context, it
from expects import expect, be_within
from src.agrovision.domain import insumo_litros_por_metro, insumo_por_hectare

# crie os testes
with description("Cálculo de insumo"):
    with context("por metro"):
        with it("calcula litros corretamente"):
            expect(insumo_litros_por_metro(10, 2, 5)).to(be_within(0.01, 100.0))
    with context("por hectare"):
        with it("calcula unidades corretamente"):
            expect(insumo_por_hectare(10, 1000)).to(be_within(0.01, 100.0))
