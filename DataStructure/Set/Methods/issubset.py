# The issubset() method returns True if all elements of the original set are present in the specified set, otherwise False.

set1 = {"apple", "banana"}
set2 = {"apple", "banana", "cherry"}
is_subset = set1.issubset(set2)
print(is_subset)  # Output: True