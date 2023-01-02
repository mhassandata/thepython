"""This tutorial covers the following topics:
Branching with if, else and elif
Nested conditions and if expressions"""

"""
Branching with if, else and elif¶
One of the most powerful features of programming languages is branching: 
    the ability to make decisions and execute a different set of statements based on whether one or more conditions are true.
"""
## The if statement
"""
In Python, branching is implemented using the if statement, which is written as follows:
if condition:
    statement1
    statement2
"""
# let see the given number is even
a_number = 34
if a_number % 2 == 0:
    print("We are inside an if block")
    print("The given nummber {} is even".format(a_number))

#the output is :We are inside an if block
#               The given nummber 34 is even