# INSTRUCTIONS

'''
Messi's Goal Total
Use variables to find the sum of the goals Messi scored in 3 competitions

Information
Messi goal scoring statistics:

Competition	Goals
La Liga	43
Champions League	10
Copa del Rey	5
Task
Create these three variables and store the appropriate values using the table above:
la_liga_goals
champions_league_goals
copa_del_rey_goals
Create a fourth variable named total_goals that stores the sum of all of Messi's goals for this year.
'''

# SOLUTION

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# RESOURCES

# https://www.codewars.com/kata/55ca77fa094a2af31f00002a

# SAMPLE TEST

'''
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(total_goals, 58, 'total goals should equal to 58')
'''
