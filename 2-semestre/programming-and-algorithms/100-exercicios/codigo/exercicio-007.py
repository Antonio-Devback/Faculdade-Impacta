"""Exercício 07 - Celsius para Fahrenheit."""


def formatar_numero(valor: float) -> str:
    """Exibe números sem zeros decimais desnecessários."""
    return f"{valor:g}".replace(".", ",")


# Valores da tabela "Teste seu programa".
casos_teste = [0, 100, -40]

for numero_teste, celsius in enumerate(casos_teste, start=1):
    fahrenheit = celsius * 9 / 5 + 32

    print(f"Teste {numero_teste}")
    print(f"Celsius: {formatar_numero(celsius)}")
    print(f"Fahrenheit: {formatar_numero(fahrenheit)}\n")
