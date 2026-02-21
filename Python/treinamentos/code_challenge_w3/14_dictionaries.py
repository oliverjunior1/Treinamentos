'''Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
Print the value of the "model" key
Add a new key "color" with the value "red"
Remove the "brand" key using pop()
Print the dictionary'''

# Create the dictionary
car = {'brand':'Ford', 'model':'Mustang', 'year':2024}
# Print the model
print(car['model'])
# Add a color key
car['color'] = 'red'
# Remove the brand key
car.pop('brand')
# Print the dictionary
print(car)