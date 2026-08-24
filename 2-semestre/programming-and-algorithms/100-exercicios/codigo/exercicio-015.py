"""Exercício 15 - Custo final da compra."""


def formatar_moeda(valor: float) -> str:
    """Formata um valor no padrão monetário brasileiro."""
    numero = f"{valor:,.2f}"
    numero = numero.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {numero}"


# Valores da tabela "Teste seu programa".
casos_teste = [(10.00, 3, 5.00), (49.90, 2, 0.00), (7.50, 10, 12.00)]

for numero_teste, (preco_unitario, quantidade, frete) in enumerate(
    casos_teste, start=1
):
    subtotal = preco_unitario * quantidade
    total = subtotal + frete

    print(f"Teste {numero_teste}")
    print(f"Preço unitário: {formatar_moeda(preco_unitario)}")
    print(f"Quantidade: {quantidade}")
    print(f"Frete: {formatar_moeda(frete)}")
    print(f"Subtotal: {formatar_moeda(subtotal)}")
    print(f"Total: {formatar_moeda(total)}\n")
