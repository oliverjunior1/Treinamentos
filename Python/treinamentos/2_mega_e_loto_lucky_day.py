import random


def mega():
    x = sorted(list(random.sample(range(1,61),6)))
    print(x)

def loto_facil():
    x = sorted(list(random.sample(range(1,26),15)))
    print(x)

def lucky_day():
    month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    x = sorted(list(random.sample(range(1,33),7)))
    y = random.choice(month)
    print(x, y)

while True:
    choice = int(input("Put 1 to mega sena, 2 to lotofacil, 3 to lucky day and 4 for exit: "))
    match choice:
        case 1:
            mega()
        case 2:
            loto_facil()
        case 3:
            lucky_day()
        case 4:
            break
        case _:
            print('Invalid number!')

