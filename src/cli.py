import typer
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm, IntPrompt, FloatPrompt
from typing import Dict, Any
from . import storage, domain

app = typer.Typer(add_completion=False)
console = Console()

def _print_table(items):
    table = Table(title="Talhões (vetor de registros)")
    table.add_column("#", justify="right")
    table.add_column("cultura")
    table.add_column("geometria")
    table.add_column("params")
    for i, it in enumerate(items):
        table.add_row(str(i), it["cultura"], it["geometria"], str(it["params"]))
    console.print(table)

@app.command()
def menu():
    """Menu interativo com loop e decisões."""
    items = storage.load()
    while True:
        console.rule("[bold green]AGROVISION[/]")
        console.print("[1] Entrada de dados")
        console.print("[2] Saída de dados (listar)")
        console.print("[3] Atualizar dado (por índice)")
        console.print("[4] Deletar dado (por índice)")
        console.print("[5] Calcular área")
        console.print("[6] Calcular insumo")
        console.print("[7] Exportar CSV (exports/agrovision.csv)")
        console.print("[0] Sair")
        op = Prompt.ask("Escolha", choices=["1","2","3","4","5","6","7","0"], default="2")

        if op == "1":
            cultura = Prompt.ask("Cultura", choices=["soja","cafe"])
            geometria = "retangulo" if cultura=="soja" else "circulo"
            if geometria == "retangulo":
                largura = FloatPrompt.ask("largura_m")
                comp    = FloatPrompt.ask("comprimento_m")
                params = {"largura_m": largura, "comprimento_m": comp}
            else:
                raio = FloatPrompt.ask("raio_m")
                params = {"raio_m": raio}
            items.append({"cultura": cultura, "geometria": geometria, "params": params})
            storage.save(items)
            console.print("[green]Registro inserido.[/]")
        elif op == "2":
            _print_table(items)
        elif op == "3":
            idx = IntPrompt.ask("Índice p/ atualizar", default=0)
            if 0 <= idx < len(items):
                it = items[idx]
                console.print(f"Atual: {it}")
                for k, v in it["params"].items():
                    nv = Prompt.ask(f"{k} (atual {v})", default=str(v))
                    it["params"][k] = float(nv)
                storage.save(items)
                console.print("[yellow]Atualizado.[/]")
            else:
                console.print("[red]Índice inválido.[/]")
        elif op == "4":
            idx = IntPrompt.ask("Índice p/ deletar", default=0)
            if 0 <= idx < len(items):
                items.pop(idx); storage.save(items)
                console.print("[red]Removido.[/]")
            else:
                console.print("[red]Índice inválido.[/]")
        elif op == "5":
            idx = IntPrompt.ask("Índice p/ área", default=0)
            try:
                it = items[idx]
                a = domain.area_m2(it["cultura"], it["geometria"], it["params"])
                console.print(f"[cyan]Área[/]: {a:.2f} m²  | {a/10_000:.4f} ha")
            except Exception as e:
                console.print(f"[red]Erro:[/] {e}")
        elif op == "6":
            modo = Prompt.ask("Tipo de cálculo", choices=["por_metro","por_hectare"])
            if modo == "por_metro":
                taxa = FloatPrompt.ask("Taxa (mL por metro)")
                n    = IntPrompt.ask("Quantas linhas (ruas)?")
                L    = FloatPrompt.ask("Comprimento de cada linha (m)")
                litros = domain.insumo_litros_por_metro(taxa, n, L)
                console.print(f"[magenta]Necessário:[/] {litros:.2f} L")
            else:
                idx  = IntPrompt.ask("Índice do talhão (usa área)")
                taxa = FloatPrompt.ask("Taxa (unid por ha)")
                it   = items[idx]
                a    = domain.area_m2(it["cultura"], it["geometria"], it["params"])
                unid = domain.insumo_por_hectare(taxa, a)
                console.print(f"[magenta]Necessário:[/] {unid:.2f} (unid do produto)")
        elif op == "7":
            import csv, pathlib
            pathlib.Path("exports").mkdir(exist_ok=True, parents=True)
            with open("exports/agrovision.csv","w",newline="",encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["idx","cultura","geometria","params_json","area_m2","area_ha"])
                for i, it in enumerate(items):
                    area = domain.area_m2(it["cultura"], it["geometria"], it["params"])
                    w.writerow([i, it["cultura"], it["geometria"], it["params"], area, area/10_000])
            console.print("[green]Exportado para exports/agrovision.csv[/]")
        else:
            console.print("[bold]Até mais![/]"); break

if __name__ == "__main__":
    app()
