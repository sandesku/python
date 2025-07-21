# A Python module is simply a file containing Python code.
# It can include functions, classes, variables, and runnable code.
# Modules allow you to organize your code into separate files, making it easier to manage and reuse across different programs.

"""
Why Use Modules?
Organization: Break down large programs into smaller, manageable pieces.
Reusability: Use the same code across multiple programs by importing the module.
Maintainability: Easier to maintain and update code in separate modules.
"""

# You can import a module into your Python program using the import statement.
# Importing the math module
import math

# Using a function from the math module
result = math.sqrt(25)
print("The square root of 25 is:", result)  # Output: The square root of 25 is: 5.0


# You can import specific functions or variables from a module using the from keyword.
# Importing only the sqrt function from the math module
from math import sqrt

# Using the imported function
result = sqrt(16)
print("The square root of 16 is:", result)  # Output: The square root of 16 is: 4.0