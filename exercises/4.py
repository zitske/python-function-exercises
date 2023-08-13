##Escreva uma função que testa se um número "a" dado é primo. Deve retornar verdadeiro apenas se "a" for primo, e falso caso contrário. Exemplo de uso: if (x>0 and primo(x)):

def primo(a):
    if a <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    
    # Verifica divisibilidade por números de 2 até a raiz quadrada de a
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False  # Se a for divisível por algum número, não é primo
    return True

numero = 8
if numero > 0 and primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
