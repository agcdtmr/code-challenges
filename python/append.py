# INSTRUCTIONS

'''
Add the value "codewars" to the websites array.
After your code executes the websites array should == ["codewars"]

The websites array has already been defined for you using the following code:

websites = []
'''

# SOLUTION

# add the value "codewars" to the already defined websites array
websites.append("codewars")

# RESOURCES

# https://www.codewars.com/kata/511f0fe64ae8683297000001

# SAMPLE TEST

'''
import codewars_test as test
from solution import websites
from preloaded import websites_internal

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.expect(websites_internal == websites, "You assigned a new array to the websites variable. You should instead alter the existing reference.")
        test.expect(len(websites_internal) > 0, 'The array is still empty')
        test.expect(len(websites_internal) == 1, 'The array contains too many values')
        test.expect(websites_internal[0] == 'codewars', 'The array does not contain the correct value "codewars"')
'''
