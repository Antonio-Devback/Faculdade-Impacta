"""Exercício 10 -   Salário com comissão."""


def formatar_moeda(valor: float) -> str:
    """Formata um valor no padrão monetário brasileiro."""
    numero = f"{valor:,.2f}"
    numero = numero.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {numero}"


# Valores da tabela "Teste seu programa".
casos_teste = [(1500.00, 5000.00), (2000.00, 0.00), (2500.00, 20000.00)]

for numero_teste, (salario_fixo, total_vendido) in enumerate(casos_teste, start=1):
    comissao = total_vendido * 0.04
    salario_total = salario_fixo + comissao

    print(f"Teste {numero_teste}")
    print(f"Salário fixo: {formatar_moeda(salario_fixo)}")
    print(f"Total vendido: {formatar_moeda(total_vendido)}")
    print(f"Comissão: {formatar_moeda(comissao)}")
    print(f"Salário total: {formatar_moeda(salario_total)}\n")
