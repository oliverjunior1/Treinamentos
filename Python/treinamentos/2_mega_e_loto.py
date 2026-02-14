import random


def mega():
    x = sorted(random.sample(range(1,61),6))
    print(x)

def lotofacil():
    x = sorted(random.sample(range(1,26),15))
    print(x)

while True:
    option = int(input("Put 1 to lotofacil, 2 to megasena and 3 to exit: "))
    match option:
        case 1:
            mega()
        case 2:
            lotofacil()
        case 3:
            break
        case _:
            print("wrong option: ")
