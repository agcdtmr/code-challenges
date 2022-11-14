# INSTRUCTIONS
'''
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"'''

# SOLUTION

def bmi(weight, height):
    result = weight / float(height * height)
    if result <= 18.5:
        return "Underweight"
    elif result <= 25.0:
        return "Normal"
    elif result <= 30.0:
        return "Overweight"
    else:
        return "Obese"

    

# RESOURCES
# https://www.codewars.com/kata/57a429e253ba3381850000fb

#SAMPLE TEST

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bmi(50, 1.80), "Underweight")
        test.assert_equals(bmi(80, 1.80), "Normal")
        test.assert_equals(bmi(90, 1.80), "Overweight")
        test.assert_equals(bmi(110, 1.80), "Obese")
        test.assert_equals(bmi(50, 1.50), "Normal")
