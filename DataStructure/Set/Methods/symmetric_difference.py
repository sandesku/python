# The symmetric_difference() method returns a new set containing elements that are in either of the sets but not in both.

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "orange"}
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {'apple', 'orange'}