# The union() method returns a new set containing all elements from the original set and all elements from the specified sets.
# It can take multiple sets or iterables as arguments.

set1 = {"apple", "banana"}
set2 = {"cherry", "banana"}
combined_set = set1.union(set2)
print(combined_set)  # Output: {'apple', 'cherry', 'banana'}