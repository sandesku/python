# Functions can also be called using keyword arguments, which allow you to specify which parameter you are setting by name.

# Defining a Function with Keyword Arguments

def create_profile(name, age, country):
    """Prints user profile information."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")

# Calling the Function with Keyword Arguments
create_profile(name="Alice", age=30, country="Canada")