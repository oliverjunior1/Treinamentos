def fun1(x):
    def fun2():
        print("##################")
        x()
        print("##################")
    return fun2

@fun1
def greetings():
    print("Jesus is the light of the world!")

greetings()