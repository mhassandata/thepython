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

"""
#Task Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

    Cost price (in Rs)                                       Tax
    > 100000                                                  15 %
    > 50000 and <= 100000                                     10%
    <= 50000                                                  5%

"""
#Conditions can also be combined using the logical operators and, or and not.
fav_number = 12
if fav_number % 3 == 0 and fav_number % 5 ==0:
    print("The {} is divisible by 3 and 5".format(fav_number))
elif not fav_number % 5 ==0:
    print("The {} is not divisible by 5".format(fav_number))
#Output: The 12 is not divisible by 5



"""
Nested if with else
In nested if's every clause must be true to reach target answer
If any of the if clause fails it will move to respective else block.
"""
#Task take input from user about the brand name and output the brand
shopping_cart = None
brand_name = input("Enter brand!. ")
if brand_name == "polo":
    shirt_color = input("Shirt color!. ")
    if shirt_color == "red":
        shirt_size = input("Shirt size!. ")
        if shirt_size == "M":
            shirt_price = int(input("Enter price!. "))
            if shirt_price < 1500:
                shopping_cart = f'{brand_name},{shirt_color},{shirt_size},{shirt_price}'
            else:
                shopping_cart = "Oho .......... Out of budget"
        else:
            shopping_cart = "Medium size is unavailable."
    else:
        shopping_cart = "Red color is not available."
else:
    shopping_cart = "Polo brand is not available now a days."

print(f"""
         ABC Shopping Centre
         ___________________
         
         Item Brand  : {brand_name}
         Item Color  : {shirt_color}
         Item Size   : {shirt_size}
         Item price  : {shirt_price}
         
         Thank your for shopping with us
         ________________________________
""")

#OUTPUT:
"""
ABC Shopping Centre
         ___________________

         Item Brand  : polo
         Item Color  : red
         Item Size   : M
         Item price  : 1250

         Thank your for shopping with us
         ________________________________
"""

#Chect whether a person is eligible for driving licence or not?
has_cnic = input("Do you have CNIC! ").lower()
has_passport = input("Do you have passport! ").lower()

if has_cnic == "yes" or has_passport == "yes":
    print("Yes you have eligibal for driving licience ")
else:
    print("You are not eligibal for driving lience")

###################################################################################################3
""""#Task Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

    Cost price (in Rs)                                       Tax
    > 100000                                                  15 %
    > 50000 and <= 100000                                     10%
    <= 50000                                                  5%
"""

# def calculate_road_tax(cost_price):
#     if cost_price > 100000:
#         tax = cost_price * 0.15
#     elif cost_price > 50000:
#         tax = cost_price * 0.1
#     else:
#         tax = cost_price * 0.05
#     return tax
cost_price = 190000
if cost_price > 100000:
    tax = cost_price * 0.15
elif cost_price > 50000:
    tax = cost_price * 0.1
else :
    tax = cost_price * 0.05
cost_price = float(input("Enter the cost price of the bike: "))
print("Road tax to be paid: Rs.", tax)


#First separate the string from digit and print it from a list
mix_list_num_string = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]
strings = [y for y in mix_list_num_string if type(y) == str]
#Output: ['A', 'B', 'C', 'D', 'E']
_____________________________________________##############################################___________________________________

