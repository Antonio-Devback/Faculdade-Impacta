"""Exercício 03 - Antecessor e sucessor."""

# Valores da tabela "Teste seu programa".
casos_teste = [1, 0, -7]

for numero_teste, numero in enumerate(casos_teste, start=1):
    antecessor = numero - 1
    sucessor = numero + 1

    print(f"Teste {numero_teste}")
    print(f"Entrada: {numero}")
    print(f"Antecessor: {antecessor}")
    print(f"Sucessor: {sucessor}\n")
