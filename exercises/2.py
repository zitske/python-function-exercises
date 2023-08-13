##Escreva uma função que receba dois números inteiros "a","b" e verifique se "a" é divisível por "b". Retornar verdadeiro caso sejam divisíveis, e falso em caso contrário. 

def verificar_divisibilidade(a, b):
    if b == 0:
        return False  # Evita divisão por zero
    return a % b == 0

numero_a = 20
numero_b = 5
if verificar_divisibilidade(numero_a, numero_b):
    print(f"{numero_a} é divisível por {numero_b}.")
else:
    print(f"{numero_a} não é divisível por {numero_b}.")
