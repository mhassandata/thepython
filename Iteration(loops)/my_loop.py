#Loop in using in python for iteration think repeating in certain conditions.
#if we need to print digit from 1 to 10
for i in range(10):
    print(i)
#The output would like  0 1 2 3 4 5 6 7 8 9
"""
Python Loops
For loop
While Loop

"""
#For loop
for i in range(10):
    print(i, "Hello World")
#It will print "Hello World" ten time.
#You will give the range funciton to start and end point like
for i in range(1, 10):
    print(i ,"Hello world")
#The difference between this loop and above are, this will start from 1 while above will start from zero.

#Now we will introduce another factor in range functio and that is step (start, end, step)
for j in range(1, 20, 2):
    print(j)
#ouput will be: 1 3 5 7 9 11 13 15 17 19

for num in range(10, 0 -2):
    print(num)
#This will display digits from 10 to 0 reverse base by steping 2 down.

#Checking the characters in full words
for char in "Pakistan":
    print(char)
#but int object is not iterable.
for item in ["Keyboard","Mouse","Monitor","Headfone","Pen","Notebook"]:
    print(item.upper())
#output: KEYBOARD MOUSE MONITOR HEADFONE PEN NOTEBOOK

items = ["Bag","Ball","Cap","Copy","Knife","Keyboard","Mouse","Monitor","Headfone","Pen","Notebook"]

for item in items:
    if item.endswith("e"):
        print(item)
    #output: Knife Mouse Headfone
for item1 in items:
    if item1.startswith("C"):
        print(item1)
    #output: Cap Copy
#let see more complex

for item in items:
    if item[-1] == "e" and (len(item) > 5):
        print(item)
#Output: Headfone

#Task
#You have to make 50 list of guest and invite them to the party
# gest_list = []
# for gust in range(10):
#     friends = input("Enter Friends name. ")
#     gest_list.append(friends)
# print(gest_list)

###### Break and Continue ##########################
for i in range(10):
    if i == 5:
        break
    print(i)
#output: 0 1 2 3 4
#Same example with "Continue"
for j in range(10):
    if j == 5:
        continue
    print(j)
#output: 0 1 2 3 4 6 7 8 9

#task: take 5 integers as input and find the sum of all integers supplied.
total = 0
for a in range(10):
    num =  int(input("Enter a number.. "))
    total += num
print(total)
#it will take 10 digit and print out the sum, now you can add average and percentage or any other calculation.


#Write program to factorize any digit 
result = 1
i = 1
while i <=100:
    result = result * i
    i += 1

print("The factorial of 100 is : {}".format(result)) 
#Output: The factorial of 100 is : 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

days = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday','Sunday']
for day in days:
    print(day)

for fruit in ['Apple', 'Orange','Banana']:
    print("Here is fruit :", fruit)
#Output:    Here is fruit : Apple
#           Here is fruit : Orange
#           Here is fruit : Banana



#Chect the value in list through iteration
for day in range(len(days)):
    print("The value at position {} is {}.".format(day, days[day]))
#Output: 
"""
The value at position 0 is Monday.
The value at position 1 is Tuesday.
The value at position 2 is Wednesday.
The value at position 3 is Thursday.
The value at position 4 is Friday.
The value at position 5 is Saturday.
The value at position 6 is Sunday.
"""
"""Another way to achieve the same result is by using the enumerate function with days as an input, 
which returns a tuple containing the index and the corresponding element."""

for i , val in enumerate(days):
     print("The value at position {} is {}.".format(i, days[i]))


#print all the list name in uppercase
list_names = ['hassan', 'zahid', 'zakir', 'adnan']
list_name_uppercase = [name.upper() for name in list_names]
print(list_name_uppercase)
#Output: ['HASSAN', 'ZAHID', 'ZAKIR', 'ADNAN']

#When we will use "for loop" and "while loop"
#### Use For loops when there's a sequence of elements that you want to iterate.For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.

#### Use while loop when you want to repeat an action until a condition changes, While loops are mostly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.


#Exercise
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)

""" Output
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]

"""

"""
Iterating using range and enumerate
The range function is used to create a sequence of numbers that can be iterated over using a for loop. It can be used in 3 ways:

range(n) - Creates a sequence of numbers from 0 to n-1
range(a, b) - Creates a sequence of numbers from a to b-1
range(a, b, step) - Creates a sequence of numbers from a to b-1 with increments of step

"""
for i in range(7):
    print(i)
for j in range(2, 12):
    print(j)
for k in range(2, 12, 2):
    print(k)


for i, val in enumerate(days):
    print('The value at position {} is {}.'.format(i, val))
"""
The value at position 0 is Monday.
The value at position 1 is Tuesday.
The value at position 2 is Wednesday.
The value at position 3 is Thursday.
The value at position 4 is Friday.
The value at position 5 is Saturday.
The value at position 6 is Sunday.

"""

# Create a list of strings: fellowship
fellowship = ["merry", "uno", "undp", "aragorn","legolas","boromir","gimli"]
# Create dict comprehension: new_fellowship
new_fellowship = { member:len(member) for memeber in fellowship}
print(new_fellowship)