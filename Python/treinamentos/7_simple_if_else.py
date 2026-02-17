while True:
    age = int(input("Put your age: "))
    print("You can't drive") if age<18 else print("You can drive. Go away!!!")