# Slicing allows you to access a range of elements from a list.
# The syntax for slicing is list[start:end],
# where start is the index to begin the slice (inclusive) and end is the index to end the slice (exclusive).

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Numbers List : ",numbers)
print("Length of numbers list : ",len(numbers))

# Slicing a list
print(numbers[2:5])  # Output: [2, 3, 4] (from index 2 to 4)

# Omitting start or end
print(numbers[:3])   # Output: [0, 1, 2] (from start to index 2)
print(numbers[5:])   # Output: [5, 6, 7, 8, 9] (from index 5 to the end)

# Slicing with a step
print(numbers[::2])  # Output: [0, 2, 4, 6, 8] (every second element)