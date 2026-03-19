import random


def mega():
    x = list(random.sample(range(1,61),6))
    print(x)

def facil():
    x = list(random.sample(range(1,26),15))
    print(x)

def luckday():
    x = list(random.sample(range(1,32),7))
    month = ['january', 'february', 'march', 'april', 'may', 'june'
             'july', 'august', 'september', 'october', 'november', 'december']
    print(x, random.choice(month))

while True:
    option = 

