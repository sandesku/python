# You can modify an existing value by referencing its key and assigning a new value.

# Example of a dictionary with strings as keys and values
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "name" : "Raj",
    "name1" : "Raju"
}

print("Before Changing : ",person)

person["name"] = "Arul"
print("After Changing", person)  # Output: 31