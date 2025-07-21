# The copy() method returns a shallow copy of the dictionary.
# This is useful if you want to work with a duplicate dictionary without affecting the original.

person = {"name": "John", "age": 31, "city": "New York"}
person_copy = person.copy()
print(person_copy)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}