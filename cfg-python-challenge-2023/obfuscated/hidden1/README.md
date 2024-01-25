# Hidden 1


# How to run hidden1.py in your terminal

```
python hidden1.py  <1st argument> < 2nd argument>
```

## How I handle this challenge

- [x] Step 1: write pseudocode from the given code
```
# F variable is assigned as float
# This line assigns the built-in float function to the variable F.
F=float

# A variable is assigned to print
# This line assigns the built-in print function to the variable A.
A=print

# using import statement it assign Module then given the alias B
# This line imports the sys module and assigns it to the variable B.
import sys as B

# C variable is assigned to B calling the argv package get the items inside the list starting 1 index
# In Python, the sys.argv list contains all the command-line arguments passed to the script. 
# The first element of this list (sys.argv[0]) is always the name of the script itself. 
# The remaining elements (sys.argv[1:]) are the command-line arguments passed to the script.
C=B.argv[1:]

# if the statement "length of C is less than 2" is true then
# A that meant to call the print function to print what's inside the quotation mark
# then if this if statement is executed use the exit function from sys Module or B. and exit this Python program
if len(C)<2:A('I require 2 numbers as input');B.exit()

# The elif statement in Python is a way of writing multiple if statements in a concise and clear manner.
# elif is used as a backup here incase the if statement above is false
# if the elif statement "length of C is greater than 2" is true then
# A that meant to call the print function to print what's inside the quotation mark
# then if this if statement is executed use the exit function from sys Module or B. and exit this Python program
elif len(C)>2:A('Stop being greedy!');B.exit()


# The try statement in Python is used to handle exceptions, which are errors that occur during the execution
# of a program. The try block contains the code that may cause an exception, and the except block contains
# the code that will run when an exception occurs

# using the try statement in Python is not because the if and elif statements are false.
# The try statement is used to handle exceptions, which are errors that occur during the execution of a program.
# If there's error with the if & elif above run the program inside the try statement
# D variable is assigned as F or using float function and convert the item in the 0 index inside the C variable then
# E variable is assigned as F or using float function and convert the item in the 1 index inside the C variable
try:D=F(C[0]);E=F(C[1])

# The except block contains the code that will run when the ValueError exception occurs or true
# which is printing the strings inside the quote then exit the program
except ValueError:A('Both numbers must be decimals');B.exit()

# An if and else statement inside an except block is a way of writing conditional logic that depends on the type or
# value of the exception that occurred in a try block.
# run this if statement is true when variable D is equal to value and data type of 0
# AND ALSO when E variable is equal to value and data type of 0 then
# print 'zero'
if D==0 and E==0:A('zero')

# when the if statement above this else is false run the program inside this else statement
# sum variable is assigned to the converting D and E variables into an absolute value then add them up
# then print sum
else:sum=abs(D)+abs(E);A(sum)
```

- [x] Step 2: Run the given code

When I run the untouched code using pycharm builtin run, it return:

```
I require 2 numbers as input

Process finished with exit code 0
```

I notice that it return a string data type. Then exit the program.

I search another way how to run a python file, as I remember when I was learning C language it was a different way to compile and execute it.

I found:

```commandline
python3 <filename> [the input asked which in this case from the output of the first run "I require 2 numbers as input"] <1stnum> <2ndnum>
```

Execution sample:
hidden1 % python3 hidden1.py 7 6
13.0
hidden1 % python3 hidden1.py 7.0 6.7
13.7
hidden1 % python3 hidden1.py 0 0
zero


- [x] Step 3: Understand the Problem

1. Do you understand what is the given input and expected output? What and how many inputs are required? 

- Input should be 2 numbers
- Check if using input() turns the 2 numbers into string datatypes and if need to be converted to integer.
- Output should be the string inside the ifs/elifs statements or the sum of the 2 absolute numbers if valueError occurs


2. What is the data type of the given input? 

- Data type is integer.

3. Create some examples.
- What’s an example input? Example input might be:
// 2, 3
- What is the output to this? To write the example output, we can write:
// 4 ---> 'I require 2 numbers as input'
// 2, 5, 3 ---> 'Stop being greedy!'
// 0 ---> 'zero'
// 3.1, 5.3 ---> 8

4. Are there any restrictions or limitations for the input? 

5. Create complex examples.
- What should we do if our inputs are different data types? ex. add('a', 'b') instead of add(2, 3)
------ // check if there are no inputs.

------ // If no inputs, return undefined.


- [x] Step 4: Break it Down or Devise a plan for solving the problem. (Pseudocode)

What would be the instruction for this challenge?

Create a Python program measuring the length of the inputs. 
Return 'I require 2 numbers as input: ' if the length is less than 2 numbers.
Return 'Stop being greedy!' if the length is greater than 2 numbers.
Use try and except block to catch the float data type errors.
Return 'zero' if the input given is 0, else return the sum of the floats in absolute form.

or 

Create a Python program that takes two decimal numbers as input and returns the sum of their absolute values


```
F=float
A=print
import sys as B
C=B.argv[1:]
if len(C)<2:A('I require 2 numbers as input');B.exit()
elif len(C)>2:A('Stop being greedy!');B.exit()
try:D=F(C[0]);E=F(C[1])
except ValueError:A('Both numbers must be decimals');B.exit()
if D==0 and E==0:A('zero')
else:sum=abs(D)+abs(E);A(sum)
```


- [x] Step 5: Write final report
What the Python programs are designed to do 
- The process and methods you used when reverse engineering the program 
- What, if any, techniques or tricks were used by the program to make reverse engineering more difficult?

Ofcourse the name haha CFG got me there.
 Obfuscation is the process of making the code more difficult to read and understand by using various techniques such as renaming variables, functions, and classes, and inserting meaningless code 
 Obfuscation of strings, resources, entry points and memory Coding signing


