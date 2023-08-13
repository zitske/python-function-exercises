##Escreva uma função que receba um número  inteiro "a" e retorne uma lista com todos os divisores de "a". Exemplo: os divisores de 12 são 12,6,4,3,2 e 1. Exemplo de uso: print(divisores(x))

def divisores(a):
    lista_divisores = []
    for i in range(1, a + 1):
        if a % i == 0:
            lista_divisores.append(i)
    return lista_divisores

numero = 12
lista_de_divisores = divisores(numero)
print(f"Os divisores de {numero} são:", lista_de_divisores)
