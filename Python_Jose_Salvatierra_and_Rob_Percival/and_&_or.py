age = 25

result = age > 18 and age < 65
print(result)

#-------------------------------
age = 25

result = age < 18 and age > 65
print(result)

#-------------------------------
age = 25

result = age < 18 and age < 65
print(result)

#-------------------------------
age = 25

result = age < 18 and age < 65
print(result)

#-------------------------------
age = 25

result = age > 18 or age < 65
print(result)

#-------------------------------

bool(0)
bool(13)

bool("")
bool("Hello")

bool([])
bool([1,3,5])

default_age = 30
age = 0

user_age = age or default_age
print(user_age)

default_greeting = "there"
name = input("Enter your name: (optional)")

user_name = name or default_greeting

print(f"Hello, {user_name}")

