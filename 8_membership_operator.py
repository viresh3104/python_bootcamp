# Membership Operators: 'in' and 'not in'

# List to check membership
fruits = ["apple", "banana", "cherry"]

# Using 'in' operator (checks if a value is present in a sequence)
membership_in = "banana" in fruits  # True because 'banana' is in the list

# Using 'not in' operator (checks if a value is not present in a sequence)
membership_not_in = "grape" not in fruits  # True because 'grape' is not in the list

# Printing the results
print(f"'banana' in fruits: {membership_in}")           # Output: True
print(f"'grape' not in fruits: {membership_not_in}")    # Output: True
