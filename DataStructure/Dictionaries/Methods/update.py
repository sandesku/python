# The update() method updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
# If a key already exists in the dictionary, its value is updated; otherwise, a new key-value pair is added.

person = {"name": "John", "age": 30, "city": "New York"}
additional_info = {"email": "john@example.com", "age": 31}
person.update(additional_info)
print(person)
# Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}