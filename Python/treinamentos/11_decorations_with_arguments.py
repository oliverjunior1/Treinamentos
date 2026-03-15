def fun1(x):
    def fun2(*args):
        print("##################################")
        x(*args)
        print("##################################")
    return fun2

@fun1
def greetings(*args):
    for arg in args:
        print(f"Hello {arg}")

greetings("Joao", "Mari")