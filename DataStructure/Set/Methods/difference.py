# The difference() method returns a new set containing elements that are in the original set but not in the specified sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "orange"}
diff_set = set1.difference(set2)
print(diff_set)  # Output: {'apple'}