# INSTRUCTIONS

'''
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
'''

# SOLUTION


def repeat_str(repeat, string):
    return string * repeat

# print(repeat_str(4, 'a'))


# RESOURCES

# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/

# SAMPLE TEST


'''
import codewars_test as test
from solution import repeat_str

@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(repeat_str(4, 'a'), 'aaaa')
        test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
        test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
    
'''

