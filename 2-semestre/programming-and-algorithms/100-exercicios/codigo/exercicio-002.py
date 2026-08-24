"""Exercício 02 - Média de duas notas."""


def formatar_decimal(valor: float) -> str:
    """Exibe o valor com uma casa decimal e vírgula."""
    return f"{valor:.1f}".replace(".", ",")


# Valores da tabela "Teste seu programa".
casos_teste = [(5.5, 7.5), (10.0, 9.0), (0.0, 4.0)]

for numero_teste, (nota_1, nota_2) in enumerate(casos_teste, start=1):
    media = (nota_1 + nota_2) / 2

    print(f"Teste {numero_teste}")
    print(f"Nota 1: {formatar_decimal(nota_1)}")
    print(f"Nota 2: {formatar_decimal(nota_2)}")
    print(f"Média: {formatar_decimal(media)}\n")
