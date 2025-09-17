class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."

Son = Family("Joao", 12)
Daughter = Family("Mariane", 4)
Wife = Family("Alyne", 39)
Me = Family("Joaquim", 42)

print(Son)
print(Daughter)
print(Wife)
print(Me)