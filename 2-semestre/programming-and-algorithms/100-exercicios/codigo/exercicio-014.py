"""Exercício 14 - Troca de valores."""

# Valores da tabela "Teste seu programa".
casos_teste = [(1, 2), (-5, 10), (7, 7)]

for numero_teste, (valor_a, valor_b) in enumerate(casos_teste, start=1):
    a_inicial = valor_a
    b_inicial = valor_b

    # O enunciado exige que a troca use uma variável auxiliar.
    auxiliar = valor_a
    valor_a = valor_b
    valor_b = auxiliar

    print(f"Teste {numero_teste}")
    print(f"A inicial: {a_inicial}")
    print(f"B inicial: {b_inicial}")
    print(f"A final: {valor_a}")
    print(f"B final: {valor_b}\n")
