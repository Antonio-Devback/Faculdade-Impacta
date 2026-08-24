"""Exercício 04 - Dobro, triplo e metade."""


def formatar_numero(valor: float) -> str:
    """Exibe números sem zeros decimais desnecessários."""
    return f"{valor:g}".replace(".", ",")


# Valores da tabela "Teste seu programa".
casos_teste = [8, 2.5, -4]

for numero_teste, valor in enumerate(casos_teste, start=1):
    dobro = valor * 2
    triplo = valor * 3
    metade = valor / 2

    print(f"Teste {numero_teste}")
    print(f"Entrada: {formatar_numero(valor)}")
    print(f"Dobro: {formatar_numero(dobro)}")
    print(f"Triplo: {formatar_numero(triplo)}")
    print(f"Metade: {formatar_numero(metade)}\n")
