class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and has {self.age} years old."

son = Family("Joao", 12)
daughter = Family("Mariane", 4)

print(son)
print(daughter)