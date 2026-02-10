def fun1(x):
    def fun2(*args):
        print("#############################")
        x(*args)
        print("#############################")
    return fun2

@ fun1
def greetings(*args):
    print(f"Hello {args}")

greetings("Joaquim")