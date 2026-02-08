import random
def mega():
    x = list(sorted(random.sample(range(1,61),6)))
    print(x)

def lotofacil():
    x = list(sorted(random.sample(range(1,26),15)))
    print(x)

while True:
    option = int(input("Type 1 to lotofacil, 2 to megasena and 3 to exit: "))

    match option:
        case 1:
            lotofacil()
        case 2:
            mega()
        case 3:
            break
        case _:
            print('Invalid number! ')


