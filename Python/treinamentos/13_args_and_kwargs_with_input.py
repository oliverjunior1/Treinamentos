def mostrar_dados(*args, **kwargs):
    print('Números informados')

    for num in args:
        print(num)

    print('\n Informações Extras:')

    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")
