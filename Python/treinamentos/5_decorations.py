def fun1(x):
    def fun2():
        print('###################')
        x()
        print('###################')
    return fun2

@fun1
def greetings():
    print("Hello Joaquim")


greetings()
greetings()
greetings()
greetings()
greetings()