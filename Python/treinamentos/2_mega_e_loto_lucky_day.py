import random


def mega():
    x = list(sorted(random.sample(range(1,61),6)))
    print(x)
def lotofacil():
    x = list(sorted(random.sample(range(1,26),15)))
    print(x)
def luckyday():
    days = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
            'november', 'december']
    x = list(sorted(random.sample(range(1,32),7)))
    y = random.choice(days)
    print(x,'month: ', y)

while True:
    option = int(input('Put 1 to mega, 2 to lotofacil, 3 to luckyday and 4 to exit: '))
    match option:
        case 1:
            mega()
        case 2:
            lotofacil()
        case 3:
            luckyday()
        case 4:
            break
        case _:
            print("Invalid number.")

