import random


def mega():
    x = sorted(list(random.sample(range(1,61),6)))
    print(x)

def facil():
    x = sorted(list(random.sample(range(1,26),15)))
    print(x)

def luckday():
    x = sorted(list(random.sample(range(1,32),7)))
    month = ['january', 'february', 'march', 'april', 'may', 'june'
             'july', 'august', 'september', 'october', 'november', 'december']
    print(x, random.choice(month))

while True:
    option = int(input('Put 1 to megasena, 2 to lotofacil, 3 to luckyday and 4 to exit: '))

    match option:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            luckday()
        case 4:
            break
        case _:
            print('Invalid number')

