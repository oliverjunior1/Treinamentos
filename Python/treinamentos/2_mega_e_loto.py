import random


def mega():
    x = sorted(list(random.sample(range(1,61),6)))
    print(x)

def lotofacil():
    x = sorted(list(random.sample(range(1,26),15)))
    print(x)

while True:
    choice = int(input("Type 1 to mega, 2 to megasena and 3 to exit: "))
    match choice:
        case 1:
            mega()
        case 2:
            lotofacil()
        case 3:
            break
        case _:
            print("Invalid number")
