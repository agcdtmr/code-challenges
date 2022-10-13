# INSTRUCTIONS

'''Write a function that will check if two given characters are the same case.

If either of the characters is not a letter, return -1
If both characters are the same case, return 1
If both characters are letters, but not the same case, return 0
Examples
'a' and 'g' returns 1

'A' and 'C' returns 1

'b' and 'G' returns 0

'B' and 'g' returns 0

'0' and '?' returns -1'''


# SOLUTION


def same_case(first, second):
    if not first.isalpha() or not second.isalpha():
        return -1
    elif first.islower() and second.islower() or first.isupper() and second.isupper():
        return 1
    else:
        return 0


print(same_case('>', '('))

# RESOURCES

# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b

#SAMPLE TEST


import codewars_test as test
from solution import same_case

@test.describe("Basic Tests")
def test_group():
    @test.it("basic test case")
    def test_case():
        test.assert_equals(same_case('C', 'B'), 1)
        test.assert_equals(same_case('b', 'a'), 1)
        test.assert_equals(same_case('d', 'd'), 1)
        test.assert_equals(same_case('A', 's'), 0)
        test.assert_equals(same_case('c', 'B'), 0)
        test.assert_equals(same_case('b', 'Z'), 0)
        test.assert_equals(same_case('\t', 'Z'), -1)
        test.assert_equals(same_case('H', ':'), -1)




