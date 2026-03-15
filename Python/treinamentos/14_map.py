# lista de números
numeros = [1,2,3,4,5]

# Função que dobra o número:
def dobrar(x):
    return x * 2

# Aplicando map
resultado = map(dobrar, numeros)

# Convertendo para lista para visualizar
resultado_lista = list(resultado)

print(resultado_lista)
