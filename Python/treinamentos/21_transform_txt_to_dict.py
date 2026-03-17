dados = {}

with open('dados.txt', 'r') as archive:
    for line in archive:
        chave, valor = line.strip().split(':')
        dados[chave] = valor

print(dados)