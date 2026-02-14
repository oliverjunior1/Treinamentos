names = ["Ana", "Carlos","Beatriz","João", "Fernando"]

big_names = list(filter(lambda names: len(names)>5, names))

print(big_names)