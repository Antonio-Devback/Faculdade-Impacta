"""Exercício 06 - Área e perímetro do retângulo."""


def formatar_numero(valor: float) -> str:
    """Exibe números sem zeros decimais desnecessários."""
    return f"{valor:g}".replace(".", ",")


# Valores da tabela "Teste seu programa".
casos_teste = [(4, 4), (2.5, 8), (10, 1)]

for numero_teste, (largura, altura) in enumerate(casos_teste, start=1):
    area = largura * altura
    perimetro = 2 * (largura + altura)

    print(f"Teste {numero_teste}")
    print(f"Largura: {formatar_numero(largura)}")
    print(f"Altura: {formatar_numero(altura)}")
    print(f"Área: {formatar_numero(area)}")
    print(f"Perímetro: {formatar_numero(perimetro)}\n")
