fruits = ["apple", "banana", "cherry"]

# Changing an item
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding an item
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Removing an item
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']