'''Create a list called fruits with: "apple", "banana", "cherry"
Write a for loop that prints each item in fruits
Use break to stop the loop when the item is "banana"'''

# Create the fruits list
fruits = ["apple", "banana", "cherry"]
# Loop through fruits, break at "banana"
for x in fruits:
    if x=='banana':
        break
    else:
        print(x)