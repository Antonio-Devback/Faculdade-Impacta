"""Exercício 01 -  Soma de dois números."""

# Valores da tabela "Teste seu programa".
casos_teste = [(4, 9), (-3, 8), (0, 12)]

for numero_teste, (primeiro_valor, segundo_valor) in enumerate(casos_teste, start=1):
    soma = primeiro_valor + segundo_valor

    print(f"Teste {numero_teste}")
    print(f"Primeiro valor: {primeiro_valor}")
    print(f"Segundo valor: {segundo_valor}")
    print(f"Soma: {soma}\n")
