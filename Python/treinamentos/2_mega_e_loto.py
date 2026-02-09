import random


def mega():
    x = list(sorted(random.sample(range(1,61),6)))
    print(x)

def facil():
    x = list(sorted(random.sample(range(1,26),15)))
    print(x)

while True:
    option = int(input("Put 1 to mega, 2 to lotofacil, and 3 to exit: "))
    match option:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            break
        case _:
            print("Not a valid number.")


