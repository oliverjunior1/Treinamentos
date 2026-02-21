'''Create a variable day with the value 3
Use a match statement to check the value of day
Add a case 3 that prints "Wednesday"
Add a wildcard case _ that prints "Other day"'''

# Create variable day
day = 3
# Use match statement

match day:
    case 3:
        print('Wednesday')
    case _:
        print('Other day')