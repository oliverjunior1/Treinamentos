dados = {}

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        chave, valor = linha.strip().split(": ")
        dados[chave] = valor

print(dados)
