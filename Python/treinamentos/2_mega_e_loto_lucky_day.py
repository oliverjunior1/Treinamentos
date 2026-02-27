import random


def mega():
    x = sorted(random.sample(range(1,61),6))
    print(x)

def facil():
    x = sorted(random.sample(range(1,26),15))
    print(x)

def lucky():
    month = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
             'august', 'september', 'october', 'november', 'december']
    x = sorted(random.sample(range(1,32),7))
    y = random.choice(month)
    print(x, y)

while True:
    option = int(input("Put 1 to lotofacil, 2 to megasena, 3 to lucky day and 4 to exit:"))
    match option:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            lucky()
        case 4:
            break
        case _:
            print("Invalid number")

