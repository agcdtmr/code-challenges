# INSTRUCTIONS

'''You need to double the integer and return it.'''

# SOLUTION

def double_integer(i):
    return i * 2

# RESOURCES

# https://www.codewars.com/kata/53ee5429ba190077850011d4

#SAMPLE TEST

import codewars_test as test

@test.describe('Tests')
def tests():
    @test.it('Sample Test Case')
    def sample_test_case():
        test.assert_equals(double_integer(2), 4);
        test.assert_equals(double_integer(4), 8);
        test.assert_equals(double_integer(-10), -20);
        test.assert_equals(double_integer(0), 0);
        test.assert_equals(double_integer(100), 200);

