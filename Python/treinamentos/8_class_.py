class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."

son = Family("Pepe", 12)
daughter = Family("Mari", 4)

print(son)
print(daughter)