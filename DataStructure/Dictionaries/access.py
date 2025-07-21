# You can access the value associated with a specific key by using the key inside square brackets [].
# Alternatively, you can use the get() method,
# which is safer because it returns None (or a default value you specify) if the key does not exist.

# Example of a dictionary with strings as keys and values
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "name" : "Raj",
    "name1" : "Raju"
}

# Accessing values using keys
name = person["name"]
print(name)  # Output: John

# Accessing values using the get() method
age = person.get("age")
print(age)  # Output: 30

# Using get() with a default value
middle_name = person.get("middle_name", "No middle name")
print(middle_name)  # Output: No middle name