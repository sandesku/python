# You can check if a key exists in a dictionary using the in keyword.

# Example of a dictionary with strings as keys and values
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "name" : "Raj",
    "name1" : "Raju"
}

if "name" in person:
    print("Name exists in the dictionary")

if "middle_name" not in person:
    print("Middle name does not exist in the dictionary")