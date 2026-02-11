def mostrar_dados(*args, **kwargs):
    print("Números informados:")

    for num in args:
        print(num)

    print("\nInformações extras:")

    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


# ===== recebendo dados do usuário =====

numeros = input("Digite números separados por espaço: ")
numeros = tuple(map(int, numeros.split()))

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

# chamando a função
mostrar_dados(*numeros, nome=nome, cidade=cidade)
