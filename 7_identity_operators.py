# Identity Operators: 'is' and 'is not'

# Assigning values to variables
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Using 'is' operator (checks if two variables point to the same object)
identity_is = a is c  # True because 'c' is the same object as 'a'

# Using 'is not' operator (checks if two variables do not point to the same object)
identity_is_not = a is not b  # True because 'a' and 'b' are different objects, even though they have the same content

# Printing the results
print(f"a is c: {identity_is}")           # Output: True
print(f"a is not b: {identity_is_not}")   # Output: True
