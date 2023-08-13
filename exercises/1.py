## Escreva uma função que calcule o valor médio de uma lista de números.

def calcular_valor_medio(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_valor_medio(numeros)
print("A média dos números é:", media)