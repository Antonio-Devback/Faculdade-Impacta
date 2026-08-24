"""Exercício 05 - Conversão de medidas."""


def formatar_numero(valor: float) -> str:
    """Exibe números sem zeros decimais desnecessários."""
    return f"{valor:g}".replace(".", ",")


# Valores da tabela "Teste seu programa".
casos_teste = [1, 0.75, 12.3]

for numero_teste, metros in enumerate(casos_teste, start=1):
    centimetros = metros * 100
    milimetros = metros * 1000

    print(f"Teste {numero_teste}")
    print(f"Metros: {formatar_numero(metros)}")
    print(f"Centímetros: {formatar_numero(centimetros)}")
    print(f"Milímetros: {formatar_numero(milimetros)}\n")
