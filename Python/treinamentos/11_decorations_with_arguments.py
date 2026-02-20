def fun1(x):
    def fun2(*args):
        print("#####################")
        x(*args)
        print("#####################")
    return fun2

@fun1
def greetings(*args):
    for a in args:
        print(f"Hello {a}")

greetings("Joaquim", "Alyne", "Joao")