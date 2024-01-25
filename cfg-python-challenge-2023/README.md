# CFG SOLVING PROBLEMS WITH PYTHON CHALLENGE 2023


## How to run the hidden.py files

You can run the program by opening a command prompt or terminal window, navigating to the directory where the program is saved, and typing the following command:

```commandline
python hidden.py <1st number> <2nd number>
```

**The challenge: PYTHON REVERSE ENGINEERING CHALLENGE**

The PYTHON REVERSE ENGINEERING Challenge with GCHQ and Code First Girls is a 4-week challenge aiming to deepen your understanding of Python programming and help gain practical skills in reverse engineering. Something used to understand Malware better and much more!

The Challenge
Join in on a multi-stage Python reverse engineering journey, exploring the intricacies of this scripting language. Python, known for its transparency during runtime, provides an ideal playground for beginners to unravel its mysteries.

Analyse 5 obfuscated Python Scripts and produce a short report describing:
1. What the Python programs are designed to do
2. The process and methods you used when reverse engineering the program
3. What, if any, techniques or tricks were used by the program to make reverse engineering more difficult

## Team or individually?

In this challenge, I decided to do it individually to challenge my Python skills after learning the basics a year ago.

## PROJECT DELIVERABLES & SUBMISSIONS

- [x] Submit this [form](https://share.hsforms.com/1sD9O0RRNQc2qAPaMQxiuaA8o274) to confirm your participation in the Solving Problems with Python Challenge - submit your registration via the form by 11.59 PM Wednesday 22nd November.
- [x] Accept the invitation to join the Slack workspace, if you haven’t already joined.
- [ ] does not need to be 100% finished
- [ ] must be able to demonstrate it via presentation, short report and Python code
- [ ] Submit your project by 11:59 pm, Tuesday  12th December, via the CFG submission form (link to be shared nearer the time)
- [ ] The slide deck should answer the challenge questions and reflect on points mentioned in the judging criteria
- [ ] Present at a live-streamed event on the 19th December  (7:30-8:30 PM)


## Videos

- [CFG MOOC Challenge - Solving Problems with PYTHON - GCHQ Kick-Off](https://www.youtube.com/watch?v=McZFDTo8kdI)


## Steps taken

- [ ] [Register at CFG MOOCs](https://codefirstgirls.com/courses/moocs/)
- [ ] Setup environment: install python & an IDE (I chose pycharm because it focus on python)
- [ ] [Learn and teach Python with PyCharm Community Edition for free](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu)
- [ ] Create a GitHub repo to organize the scripts, my documentation and resources in one place.
- [ ] Read: [How to Solve a Coding Challenge as a Beginner](https://medium.com/codex/how-to-solve-a-coding-challenge-as-a-beginner-c6686d12c3f9) by Eva Yi Zheng
- [ ] Read: [How to Solve Coding Problems with a Simple Four Step Method](https://www.freecodecamp.org/news/how-to-solve-coding-problems/) by Madison Kanna
- [ ] [How To Approach A Coding Problem?](https://www.geeksforgeeks.org/how-to-approach-a-coding-problem/)
- [ ] [How to Get Better At Solving Coding Challenges](https://www.microverse.org/blog/how-to-get-better-at-solving-coding-challenges) by Ahmad Muhammad
- [ ] Attend the kick-off
- [ ] Review [Kick-off Presentation](https://docs.google.com/presentation/d/1VFDwwjNSe0bVD_GYOnW6xhyww1ECzhvu/edit#slide=id.g1418c291be1_0_56)
- [ ] Clarifying questions about the challenge
- [ ] [Obfuscated](https://drive.google.com/drive/folders/1PFXixsEkQmKRBBtX9hn1x3P_bdEhSlQa)

## Clarifying questions about the challenge

1. Can we use any method/technique on solving this coding challenge?
2. 


## Step by step guide how to solve the given python challenges

### Understand the Problem
Do you understand what is the given input and expected output?
What kinds of inputs will go into this problem? ex. Will the inputs always be just two numbers? What should happen if our function receives as input three numbers?
you could write down possible inputs in a code comment to get a sense of what they’ll look like:
//inputs: 2, 4

What are the outputs?


Are there any restrictions or limitations for the input?
What is the data type of the given input?
How to label the function(s)/parameter(s)/other variables?
Did you understand the problem fully?
Would you be able to explain this question to someone else?
What and how many inputs are required?
What would be the output for those inputs
Do you need to separate out some modules or parts from the problem?
Do you have enough information to solve that question? If not then read the question again or clear it to the interviewer.

Create some examples.
What’s an example input? Example input might be:
// add(2, 3)
What is the output to this? To write the example output, we can write:
// add(2, 3) ---> 5


Create complex examples.
what should we do if our inputs are different data types? ex. add('a', 'b') instead of add(2, 3)
// check if there are no inputs.

// If no inputs, return undefined.

it’s good to think about edge cases

Computer science professor Evans says to write what developers call defensive code. Think about what could go wrong and how your code could defend against possible errors.  



### Break it Down or Devise a plan for solving the problem.
write it out in pseudocode.

Pseudocode is a plain language description of the steps in an algorithm. In other words, your pseudocode is your step-by-step plan for how to solve the problem. In CFG's case, how you understand the given script.

Try using comments to break down the steps of the algorithm. Comment the layout of the if statements/loops/methods you plan on using.

What would be the instruction for this challenge? ex. Create a function that adds together two numbers and returns that value.

clarify any part of it you do not understand. 

read through the problem out loud

### Solve/Simplify
write out your actual code.
Try coding the solution with the comments! If you can’t write the whole solution, simplify the solution.

Professor Evans suggests focusing on a simple, mechanical solution. The easier and simpler your solution is, the more likely you can program it correctly.

What if you can’t solve the entire problem? What if there's a part of it you still don't know how to solve?

Colt Steele gives great advice here: If you can’t solve part of the problem, ignore that hard part that’s tripping you up. Instead, focus on everything else that you can start writing.

For more complex problems, professor Evans notes, “Consider systematically how a human solves the problem.” That is, forget about how your code might solve the problem for a moment, and think about how you would solve it as a human. This can help you see the steps more clearly.

### Write final report
- What the Python programs are designed to do 
- The process and methods you used when reverse engineering the program 
- What, if any, techniques or tricks were used by the program to make reverse engineering more difficult


### Refactor (as needed) or Look back over what you've done

Is your code easy to read?
Is it intuitive?
Can you think of another way to solve it?
Do you get the expected outputs for all cases that you can think of?
How do you think other people will solve it?


As you look at your work, here are some questions Colt Steele suggests you ask yourself to figure out how you can improve your solution:

Can you derive the result differently? What other approaches are there that are viable?
Can you understand it at a glance? Does it make sense?
Can you use the result or method for some other problem?
Can you improve the performance of your solution?
Can you think of other ways to refactor?
How have other people solved this problem?


Does this code run for every possible input including the edge cases.
Is there an alternate solution for the same problem?
Is the code efficient? Can it be more efficient or can the performance be improved?
How else can you make the code more readable?
Are there any more extra steps or functions you can take out?
Is there any repetition in your code? Take it out.

### Dry-run your solution. Code & Test
Dry-running a solution on test cases and edge cases


### Submit the solution

Double check the documentation


## Planning

- Nov 23 & 24: Researching & Planning
- Nov 27, 28, 29: hidden1.py
- Nov 29, 30, Dec 1: hidden2.py
- Dec 3, 5, 6: hidden3.py
- Dec 6, 7, 8: hidden4.py
- Dec 8, 11, 12: hidden5.py
- Dec 12: Submission
- Dec 15: Announcement of 3 finalists
- Dec 19: Presentation


## template

```commandline
1. Do you understand what is the given input and expected output? 
2. What kinds of inputs will go into this problem?
3. What are the outputs?
4. Are there any restrictions or limitations for the input? 
5. What is the data type of the given input? 
6. How to label the function(s)/parameter(s)/other variables? 
7. Did you understand the problem fully? 
8. Would you be able to explain this question to someone else? 
9. What and how many inputs are required? 
10. What would be the output for those inputs 
11. Do you need to separate out some modules or parts from the problem? 
12. Do you have enough information to solve that question? If not then read the question again or clear it to the interviewer. 
13. Create some examples.
- What’s an example input? Example input might be:
// add(2, 3)
- What is the output to this? To write the example output, we can write:
// add(2, 3) ---> 5
14. Create complex examples.
- What should we do if our inputs are different data types? ex. add('a', 'b') instead of add(2, 3)
------ // check if there are no inputs.

------ // If no inputs, return undefined.
```