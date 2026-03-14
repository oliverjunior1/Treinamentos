def fun1(x):
    def fun2(*args):
<<<<<<< HEAD
        print("###########################")
        x(*args)
        print("###########################")
=======
        print("###################################")
        x(*args)
        print("###################################")
>>>>>>> 386c48ab190b6e688be8e2c587f15a8d25e9912a
    return fun2

@fun1
def greetings(*args):
    for arg in args:
        print(f"Hello {arg}")
<<<<<<< HEAD
        print("###########################")

greetings('Alyne', 'Pepe', 'Mari', 'Joaquim')
=======

greetings("Alyne", "Joao", "Mari")

>>>>>>> 386c48ab190b6e688be8e2c587f15a8d25e9912a
