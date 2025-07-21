# The pop() method removes and returns a random element from the set.
# Since sets are unordered, you don't know which element will be removed.
# If the set is empty, it raises a KeyError.

fruits = {"apple", "banana", "cherry"}
removed_fruit = fruits.pop()
print(removed_fruit)  # Output: Random element (e.g., 'apple')
print(fruits)         # Output: Remaining elements