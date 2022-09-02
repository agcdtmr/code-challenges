# INSTRUCTIONS

# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# SOLUTION

def grow(arr):
    multiplier = 1
    for i in arr:
        multiplier = multiplier * i
    return multiplier

# RESOURCES

# https://www.codewars.com/kata/57f780909f7e8e3183000078