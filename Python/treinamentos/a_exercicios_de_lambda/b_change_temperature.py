"""🧠 Exercício: Transformando Temperaturas
com lambda
Você recebeu uma lista de temperaturas em graus Celsius
e precisa convertê-las para Fahrenheit usando map() e uma função lambda.
"""
# Lista de temperaturas em Celsius
celsius = [0, 10, 20, 30, 40]

# Usando map e lambda para converter para Fahrenheit
fahrenheit = list(map(lambda c: round(c * 9 / 5 + 32, 1), celsius))

print(fahrenheit)

