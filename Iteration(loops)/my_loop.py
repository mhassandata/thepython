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
