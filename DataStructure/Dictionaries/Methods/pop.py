# The pop() method removes the specified key and returns the corresponding value.
# If the key is not found, a KeyError is raised unless a default value is provided.

person = {"name": "John", "age": 30, "city": "New York"}

age = person.pop("age")
print(age)  # Output: 31
print(person)  # Output: {'name': 'John', 'city': 'New York', 'email': 'john@example.com'}

# Using pop with a default value
middle_name = person.pop("middle_name", "No middle name")
print(middle_name)  # Output: No middle name