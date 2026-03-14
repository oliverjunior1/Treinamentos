list_names = ['Joaquim', 'Daniela', 'João','Ivan', 'Amarildo']

big_names = list(filter(lambda a: len(a)>5, list_names))

print(big_names)