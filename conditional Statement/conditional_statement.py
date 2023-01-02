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

#As expected, since the condition another_number % 2 == 0 evaluates to False, no message is printed.

"""The else statement
We may want to print a different message if the number is not even in the above example. This can be done by adding the else statement. 
It is written as follows:

if condition:
    statement1
    statement2
else:
    statement4
    statement5
If condition evaluates to True, the statements in the if block are executed. 
If it evaluates to False, the statements in the else block are executed."""
a_number_1 = 59
if a_number_1 % 2 ==0:
    print("{} is a even number".format(a_number_1))
else:
    print("{} is an odd number".format(a_number_1))
#output is : 59 is an odd number


#Task
#Write a program to check whether a person is eligible for voting or not.(voting age >=18)

user_age = int(input("Enter a age...! "))
if user_age >= 18:
    print("Congratulations You are eligibal for vote")
else:
    print("Oh You are not eligibal try next year.")

# The elif statement
"""" 
Python also provides an elif statement (short for "else if") to chain a series of conditional blocks. 
The conditions are evaluated one by one. For the first condition that evaluates to True, the block of statements below it is executed. 
The remaining conditions and statements are not evaluated. So, in an if, elif, elif... chain, at most one block of statements is executed, 
the one corresponding to the first condition that evaluates to True
"""

today = 'Wednesday'
if today == 'Sunday':
    print("Today is the day of the sun.")
elif today == 'Monday':
    print("Today is the day of the moon.")
elif today == 'Tuesday':
    print("Today is the day of Tyr, the god of war.")
elif today == 'Wednesday':
    print("Today is the day of Odin, the supreme diety.")
elif today == 'Thursday':
    print("Today is the day of Thor, the god of thunder.")
elif today == 'Friday':
    print("Today is the day of Frigga, the goddess of beauty.")
elif today == 'Saturday':
    print("Today is the day of Saturn, the god of fun and feasting.")
#Output: Today is the day of Odin, the supreme diety.

"""In the above example, the first 3 conditions evaluate to False, 
so none of the first 3 messages are printed. 
The fourth condition evaluates to True, so the corresponding message is printed. The remaining conditions are skipped. 
Try changing the value of today above and re-executing the cells to print all the different messages."""

my_number = 15
if my_number % 2 == 0:
    print("{} is divisible by 2".format(my_number))
elif my_number % 3 == 0:
    print("{} is divisible by 3".format(my_number))
elif my_number % 4 == 0:
    print("{} is divisible by 4".format(my_number))
elif my_number % 5 == 0:
    print("{} is divisible by 5".format(my_number))
else:
    print("None of above")

#1Ouput: 15 is divisible by 3
#But you notice that 15 is also divisible by 5 which is not evaluated so below we will see the following condition
if my_number % 2 == 0:
    print("{} is divisible by 2".format(my_number))
if my_number % 3 == 0:
    print("{} is divisible by 3".format(my_number))
if my_number % 4 == 0:
    print("{} is divisible by 4".format(my_number))
if my_number % 5 == 0:
    print("{} is divisible by 5".format(my_number))
else:
    print("None of above")
#output:    15 is divisible by 3
#           15 is divisible by 5

