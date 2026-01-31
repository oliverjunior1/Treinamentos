import random


def mega():
    x = sorted(random.sample(range(1,61),6))
    return x
def lotofacil():
    x = sorted(random.sample(range(1,26),15))
    return x

print(lotofacil())
