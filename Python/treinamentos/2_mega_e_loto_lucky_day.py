import random


def mega():
    x = sorted(random.sample(range(1,61),6))
    print(x)
def facil():
    x = sorted(random.sample(range(1,26),15))
    print(x)
def lucky_day():
    x = sorted(random.sample(range(1,34),7))
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']
    months_random = random.choice(months)
    print(x, months_random)

while True:
    option = int(input('For megasena put 1, for lotofacil put 2, for luckyday put 3 and for exit, put 4: '))
    match option:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            lucky_day()
        case 4:
            break
        case _:
            print("Invalid number")
