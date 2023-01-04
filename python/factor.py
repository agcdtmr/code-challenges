# INSTRUCTIONS

'''
About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: 2 * 3 = 6

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder
For example 2 is not a factor of 7 because: 7 % 2 = 1

Note: base is a non-negative number, factor is a positive number.
'''

# SOLUTION


def check_for_factor(base, factor):
    return base % factor == 0

# RESOURCES

# https://www.codewars.com/kata/55cbc3586671f6aa070000fb

# SAMPLE TEST


'''
import codewars_test as test
from solution import check_for_factor

@test.describe("Fixed Tests")
def fixed_tests():    
    @test.it("Should return True")
    def should_return_true():
        test.assert_equals(check_for_factor(10, 2), True)
        test.assert_equals(check_for_factor(63, 7), True)
        test.assert_equals(check_for_factor(2450, 5), True)
        test.assert_equals(check_for_factor(24612, 3), True)
        
    @test.it("Should return False")
    def should_return_false():
        test.assert_equals(check_for_factor(9, 2), False)
        test.assert_equals(check_for_factor(653, 7), False)
        test.assert_equals(check_for_factor(2453, 5), False)
        test.assert_equals(check_for_factor(24617, 3), False)
'''
