class Person:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

    def __str__(self):
        return f"The name is {self.name} {self.lname} and the age is {self.age}."

person = Person("Joao", "Pedro", 12)

print(person)