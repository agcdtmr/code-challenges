# INSTRUCTIONS

'''
Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
'''

# SOLUTION


def capitals(word):
    str_index = []
    for index, str in enumerate(word):
        if str.isupper():
            str_index.append(index)
    return str_index

# RESOURCES


#https://www.codewars.com/kata/539ee3b6757843632d00026b/

# SAMPLE TEST


'''
import codewars_test as test
from solution import capitals

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals( capitals('CodEWaRs'), [0,3,4,6] )
'''
