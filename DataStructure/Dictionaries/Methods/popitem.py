# The popitem() method removes and returns the last inserted key-value pair as a tuple.
# This method is particularly useful for dictionaries that maintain insertion order (Python 3.7+).

person = {"name": "John", "age": 30, "city": "New York"}

last_item = person.popitem()
print(last_item)  # Output: ('email', 'john@example.com')
print(person)     # Output: {'name': 'John', 'city': 'New York'}