'''🧠 Exercício: Filtrando Números Primos com lambda
Crie uma função que recebe uma lista de números inteiros e retorna apenas
os números primos usando filter() e lambda uma função lambda.
💡 Dica:
Você pode usar uma função auxiliar para verificar se um número é primo,
mas o filtro deve ser feito com lambda.'''

# Função auxiliar para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Lista de entrada
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Filtrando os primos com lambda e filter
primos = list(filter(lambda x: eh_primo(x), numeros))

print(primos)