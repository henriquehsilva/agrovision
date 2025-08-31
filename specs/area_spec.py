# specs/area_spec.py
# -*- coding: utf-8 -*-
from mamba import description, context, it
from expects import expect, be_within
from src.agrovision.domain import area_m2

with description("Cálculo de área"):
    with context("soja (retângulo)"):
        with it("largura x comprimento"):
            a = area_m2("soja", "retangulo", {"largura_m": 10, "comprimento_m": 20})
            expect(a).to(be_within(200 - 1e-4, 200 + 1e-4))  # [199.9999, 200.0001]

    with context("café (círculo)"):
        with it("pi * r^2"):
            a = area_m2("cafe", "circulo", {"raio_m": 5})
            expect(a).to(be_within(78.5398163397 - 1e-3, 78.5398163397 + 1e-3))
