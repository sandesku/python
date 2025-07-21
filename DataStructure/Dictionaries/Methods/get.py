# The get() method returns the value for the specified key if the key is in the dictionary.
# If the key is not found, it returns None (or a specified default value).

person = {"name": "John", "age": 30, "city": "New York"}

city = person.get("city")
print(city)  # Output: New York

middle_name = person.get("middle_name", "No middle name")
print(middle_name)  # Output: No middle name