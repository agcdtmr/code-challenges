# INSTRUCTIONS

# Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.

# Examples:
# 42, "int"    --> True
# "42", "int"  --> False

# SOLUTION

def type_validation(variable, _type): 
    return _type in str(type(variable))

# RESOURCES

# https://www.codewars.com/kata/59c1302ecb7fb48757000013