# The issuperset() method returns True if the original set contains all elements of the specified set, otherwise False.

set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "banana"}
is_superset = set1.issuperset(set2)
print(is_superset)  # Output: True