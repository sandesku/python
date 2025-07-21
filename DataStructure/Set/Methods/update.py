# The update() method adds multiple elements to the set.
# You can pass a list, tuple, set, or any iterable as an argument.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "grape"]
fruits.update(more_fruits)
print(fruits)  # Output: {'apple', 'orange', 'banana', 'grape', 'cherry'}