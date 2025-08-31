from mamba import description, context, it
from expects import expect, be_within
from src.agrovision.domain import area_m2

with description("Cálculo de área"):
    with context("soja (geometria: retângulo)"):
        with it("calcula largura x comprimento"):
            a = area_m2("soja", "retangulo", {"largura_m": 10, "comprimento_m": 20})
            expect(a).to(be_within(200, 1e-4))

    with context("café (geometria: círculo)"):
        with it("calcula pi · r^2"):
            a = area_m2("cafe", "circulo", {"raio_m": 5})
            expect(a).to(be_within(78.5398, 1e-3))
