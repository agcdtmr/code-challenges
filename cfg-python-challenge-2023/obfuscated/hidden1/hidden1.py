# F=float
# A=print
# import sys as B
# C=B.argv[1:]
# if len(C)<2:A('I require 2 numbers as input');B.exit()
# elif len(C)>2:A('Stop being greedy!');B.exit()
# try:D=F(C[0]);E=F(C[1])
# except ValueError:A('Both numbers must be decimals');B.exit()
# if D==0 and E==0:A('zero')
# else:sum=abs(D)+abs(E);A(sum)


# # Create a Python program measuring the length of the inputs.
# # Return 'I require 2 numbers as input: ' if the length is less than 2 numbers.
# # Return 'Stop being greedy!' if the length is greater than 2 numbers.
# # Use try and except block to catch the float data type errors.
# # Return 'zero' if the input given is 0, else return the sum of the floats in absolute form.
# #
# # or
# #
# # Create a Python program that takes two decimal numbers as input and returns the sum of their absolute values








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



# The process and methods you used when reverse engineering the program


# correct the syntax
#
#
# Reverse engineering an obfuscated Python program involves unraveling its logic and structure to understand how it works despite attempts to obscure the code. Here are some methods and processes commonly used:
#
# ### Static Analysis:
# 1. **Decompilation**: Tools like uncompyle6, PyInstaller Extractor, or uncompyle2 can help decompile Python bytecode back into a higher-level representation.
# 2. **Code Review**: Manually examining the code to identify patterns, logic, and structures despite obfuscation.
# 3. **Static Code Analysis Tools**: Using tools like Pylint, Pyflakes, or Bandit can help identify potential vulnerabilities or suspicious code patterns.
#
# ### Dynamic Analysis:
# 1. **Debugger**: Utilize debuggers like pdb, PyCharm debugger, or Winpdb to step through the code, observe variables, and understand execution flow.
# 2. **Runtime Analysis**: Employing tools like pyrasite or Python's `trace` module to inspect code behavior during runtime.
# 3. **Dynamic Instrumentation**: Tools like Frida or Dyninst can dynamically modify code behavior to aid analysis.
#
# ### Obfuscation Techniques and Countermeasures:
# 1. **String Manipulation**: Reversing string manipulations (encryption, encoding, etc.) to reveal the original code.
# 2. **Control Flow Obfuscation**: Identifying and reconstructing altered control flows to understand the program logic.
# 3. **Renaming Variables/Functions**: Mapping and renaming obfuscated variables/functions to meaningful names.
# 4. **Code Compression/Encryption**: Decompressing or decrypting code sections to restore readability.
# 5. **Anti-Debugging Techniques**: Analyzing and bypassing techniques used to hinder debugging and analysis.
#
# ### Automated Tools and Libraries:
# 1. **Disassemblers and Decompilers**: Ghidra, IDA Pro, Radare2 are powerful tools that assist in disassembling and analyzing the binary/executable.
# 2. **Scripting Languages**: Writing custom scripts in Python or other languages to automate certain reverse engineering tasks.
#
# ### Iterative Approach:
# 1. **Step-by-Step Analysis**: Break down the code into smaller parts for easier understanding.
# 2. **Documentation and Annotation**: Documenting findings and hypotheses during the reverse engineering process aids in reconstructing the code's logic.
#
# ### Challenges and Considerations:
# 1. **Complexity**: Some obfuscation techniques can make code extremely convoluted, making it challenging to decipher.
# 2. **Legal and Ethical Concerns**: Ensure compliance with laws and ethical considerations while reverse engineering.
#
# Reverse engineering obfuscated code can be time-consuming and challenging, often requiring a combination of different methods and tools depending on the level of obfuscation applied to the code.
