# You can remove a key-value pair using the del keyword or the pop() method.

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "name" : "Raj",
    "name1" : "Raju"
}

# Using del
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'email': 'john@example.com'}

# Using pop()
email = person.pop("email")
print(email)   # Output: john@example.com
print(person)  # Output: {'name': 'John', 'age': 31}