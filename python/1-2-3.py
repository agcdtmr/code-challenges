# INSTRUCTIONS

'''Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]'''

# SOLUTION

def number(lines):
    outputList = []
    for index in range(0, len(lines)):
        output = str(index + 1) + ': ' + str(lines[index])
        outputList.append(output)
    return outputList

# RESOURCES

# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9

#SAMPLE TEST

import codewars_test as test
from solution import number

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(number([]), [])
        test.assert_equals(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])
