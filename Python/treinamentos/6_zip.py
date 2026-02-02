list_1 = ['name', 'age', 'profession']
list_2 = ['Pepe', 12, 'gamer']
dict_union = {}
for x, y in zip(list_1, list_2):
    dict_union[x] = y

print(dict_union)