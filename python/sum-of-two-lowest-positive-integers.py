# INSTRUCTIONS

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.


# SOLUTION

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


# RESOURCES

# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python


#SAMPLE TEST

# import codewars_test as test
# from solution import sum_two_smallest_numbers

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
#         test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
#         test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)

