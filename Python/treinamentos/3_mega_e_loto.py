import random


def mega():
    x = sorted(random.sample(range(1,61),6))
    return x
def lotofacil():
    x = sorted(random.sample(range(1,26),15))
    return x

while True:
    choice = int(input('Put 1 to megasena, 2 to lotofacil and 3 to exit: '))
    match choice:
        case 1:
            print(mega())
        case 2:
            print(lotofacil())
        case 3:
            break

