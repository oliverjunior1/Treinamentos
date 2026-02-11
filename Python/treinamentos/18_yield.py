def contador():
    yield 1
    yield 2
    yield 3

for num in contador():
    print(num)
