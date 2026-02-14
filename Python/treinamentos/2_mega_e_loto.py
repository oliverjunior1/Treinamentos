import random


def mega():
    x = sorted(random.sample(range(1,61),6))
    print(x)

def lotofacil():
    x = sorted(random.sample(range(1,26),15))
    print(x)

def lucky_day():
    months = ["jan", 'fev', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'octo', 'nov', 'dec']
    x = sorted(random.sample(range(1,32),7))
    y = random.choice(months)
    print(x, y)

while True:
    option = int(input("Put 1 to lotofacil, 2 to megasena and 3 to luckyday, and 4 to exit: "))
    match option:
        case 1:
            mega()
        case 2:
            lotofacil()
        case 3:
            lucky_day()
        case 4:
            break
            
