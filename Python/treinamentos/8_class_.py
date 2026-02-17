class Family:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."

son = Family("Joao",12)
daughter = Family("Mariane", 4)

print(son)
print(daughter)