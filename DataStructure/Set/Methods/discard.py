# The discard() method removes a specified element from the set.
# If the element is not found, it does nothing (no error is raised).

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
fruits.discard("mango")  # No error, even though "mango" is not in the set
print(fruits)  # Output: {'apple', 'cherry'}