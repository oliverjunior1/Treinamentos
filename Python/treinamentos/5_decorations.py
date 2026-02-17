def fun1(x):
    def fun2():
        print("###################")
        x()
        print("###################")
    return fun2

@fun1
def greetings():
    print("I love you Jesus.")

greetings()
greetings()
greetings()
greetings()
