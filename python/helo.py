# INSTRUCTIONS

'''
Debugging sayHello function
The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

Example output:

Hello, Mr. Spock
'''

# SOLUTION


def say_hello(name):
    return "Hello, %s" % (name)

# RESOURCES

# https://www.codewars.com/kata/5625618b1fe21ab49f00001f

# SAMPLE TEST


'''
import codewars_test as test
from solution import say_hello

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(say_hello('Mr. Spock'), 'Hello, Mr. Spock')
        test.assert_equals(say_hello('Captain Kirk'), 'Hello, Captain Kirk')
        test.assert_equals(say_hello('Liutenant Uhura'), 'Hello, Liutenant Uhura')
        test.assert_equals(say_hello('Dr. McCoy'), 'Hello, Dr. McCoy')
        test.assert_equals(say_hello('Mr. Scott'), 'Hello, Mr. Scott')
'''
