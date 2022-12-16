# INSTRUCTIONS

'''
Summation
Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
'''

# SOLUTION


def summation(num):
    result = 0
    count = 1

    while count <= num:
        result += count
        count += 1
    return result


# RESOURCES

# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/

# SAMPLE TEST

# print(summation(48))

'''
if __name__ == '__main__':

    ### TEST CASES ###

    # test case 1
    assert summation(1) == 1

    # test case 2
    assert summation(8) == 36
'''


'''
import codewars_test as test
from solution import summation

@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(summation(1), 1)
        test.assert_equals(summation(8), 36)
        test.assert_equals(summation(22), 253)
        test.assert_equals(summation(100), 5050)
        test.assert_equals(summation(213), 22791)

'''
