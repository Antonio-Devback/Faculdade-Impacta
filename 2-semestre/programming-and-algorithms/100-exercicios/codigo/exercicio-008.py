"""Exercício 08 - Desconto no produto."""


def formatar_moeda(valor: float) -> str:
    """Formata um valor no padrão monetário brasileiro."""
    numero = f"{valor:,.2f}"
    numero = numero.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {numero}"


# Valores da tabela "Teste seu programa".
casos_teste = [50.00, 99.90, 1000.00]

for numero_teste, preco in enumerate(casos_teste, start=1):
    desconto = preco * 0.10
    preco_final = preco - desconto

    print(f"Teste {numero_teste}")
    print(f"Preço: {formatar_moeda(preco)}")
    print(f"Desconto: {formatar_moeda(desconto)}")
    print(f"Preço final: {formatar_moeda(preco_final)}\n")
