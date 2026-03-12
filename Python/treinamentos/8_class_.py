class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."


Son = Family("Joao", 12)
Daughter = Family("Mari", 4)

print(Son)
print(Daughter)