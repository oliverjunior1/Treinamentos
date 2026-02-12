dados = {}

with open('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        chave, valor = linha.strip().split(':')
        dados[chave] = valor

print(dados)
