import random


def mega():
    lucky = sorted(random.sample(range(1,61),6))
    print(lucky)

def lotofacil():
    lucky = sorted(random.sample(range(1,26),15))
    print(lucky)

def lucky_day():
    month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
             'november', 'december']
    random_month = random.choice(month)
    lucky = sorted(random.sample(range(1,34),7))
    print(lucky, random_month)

while True:
    option = int(input("Put 1 to megasena, 2 to lotofacil, 3 to lucky day and 4 to exit: "))
    match option:
        case 1:
            mega()
        case 2:
            lotofacil()
        case 3:
            lucky_day()
        case 4:
            break
        case _:
            print("Invalid number!")

