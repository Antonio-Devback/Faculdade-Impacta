"""Exercício 09 - Reajuste salarial."""


def formatar_moeda(valor: float) -> str:
    """Formata um valor no padrão monetário brasileiro."""
    numero = f"{valor:,.2f}"
    numero = numero.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {numero}"


# Valores da tabela "Teste seu programa".
casos_teste = [1200.00, 3500.00, 800.00]

for numero_teste, salario_atual in enumerate(casos_teste, start=1):
    aumento = salario_atual * 0.15
    novo_salario = salario_atual + aumento

    print(f"Teste {numero_teste}")
    print(f"Salário atual: {formatar_moeda(salario_atual)}")
    print(f"Aumento: {formatar_moeda(aumento)}")
    print(f"Novo salário: {formatar_moeda(novo_salario)}\n")
