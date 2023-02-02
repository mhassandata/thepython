# -*- coding: utf-8 -*-
"""Bit-Dev Class1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IQaQVRsjXEwx9BG_po7DPG_ShqA2bLk9

# Python Crash Course

Please note, this is not meant to be a comprehensive overview of Python or programming in general, 

This notebook is meant to get the mentees up to speed with the very basics of python3 in the topics mentioned below;

This notebook will just go through the basic topics in order:

* House cleaning:
    * Local requirements
    * Python installation
    * jupyter installation
    
    

* Data types
    * Numbers
    * Strings
    * Printing
    * Lists
    * Dictionaries
    * Booleans
    * Tuples 
    * Sets
* Comparison Operators
* if,elif, else Statements
* for Loops
* while Loops
* range()
* list comprehension
* functions
* lambda expressions
* map and filter
* methods
____

# Local Requirements

In order to run the examples in this class, you will need a python environment set up on your local machine:
For this, you can either use the official *python3* distribution or the *Anaconda Distribution*

We recommend using the anaconda distribution as this comes with most of the necessary libraries pre-installed.

## Installing Anaconda

Anaconda is a Python distribution for data science and machine learning. It is free and open-source and makes managing and deploying packages simple.
It has more than 1000 data science packages and the Conda package. Other tools it comes with are core Python, IPython, among others.

To download an Anaconda distribution, you can use the official download page:
https://www.anaconda.com/download/
Here, you can select your platform and then choose the installer. For this, you can choose which version you want and whether 32-bit or 64-bit.
To install a package with conda, you can use the following command on CMD or on your terminal –

`` conda install scipy ``

## Jupyter Notebooks

Jupyter notebooks ships with Anaconda, so in order to launch it, simply use the command below from your terminal or command prompt:

``jupyter notebook``

This will launch a browser window on your computer which you can use

# Introduction to Python

The key building blocks of the python programming language are the data types, these include numbers,lists, strings etc as shown below

## Data types

### Numbers
"""

1 + 1

1 * 3

1 / 2

2 ** 4

4 % 2

5 % 2

(2 + 3) * (5 + 5)

"""### Variable Assignment"""

# Can not start with number or special characters
name_of_var = 2

x = 2
y = 3

z = x + y

z

"""### Strings"""

'single quotes'

"double quotes"

" wrap lot's of other quotes"

"""### Printing"""

x = 'hello'

x

print(x)

num = 12
name = 'Sam'

print('My number is: {one}, and my name is: {two}'.format(one=num,two=name)

print('My number is: {}, and my name is: {}'.format(num,name))

age = 27
my_name = "Muhammad Hassan"
print(f"My name is {my_name}, and my age is {age}")

age = 27
my_name = "Muhammad Hassan"
print(f"My name is {my_name}, and my age is {age}")

"""### Lists"""

[1,2,3]

['hi',1,[1,2]]

my_list = ['a','b','c']

my_list.append('d')

my_list

my_list.insert(2, "m")
my_list

my_list[0]

my_list[1]

my_list[1:]

my_list[:1]

my_list[0] = 'NEW'

my_list

nest = [1,2,3,[4,5,['target']]]
nest

nest[3]

nest[3][2]

nest[3][2][0]

"""### Dictionaries"""

d = {'key1':'item1','key2':'item2'}

d

d['key1']

import pandas as pd

my_dict = {
    "Names" : ["Mohd", "Asad", "Zahid", "Salman"],
    "Marks" : [55,66,77,88],
    "CGPA" : [2.5, 3.0, 3.2, 3.5]
}
df = pd.DataFrame(my_dict)
df

"""### Booleans"""

True

False

"""### Tuples """

t = (1,2,3)

t[0] = 'NEW'

t[0]

"""### Sets"""

{1,2,3}

{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}

"""## Comparison Operators"""

1 > 2

1 < 2

1 >= 1

1 <= 4

1 == 1

'hi' == 'bye'

"""## Logic Operators"""

(1 > 2) and (2 < 3)

(1 > 2) or (2 < 3)

(1 == 2) or (2 == 3) or (4 == 4)

(1 == 2) or (2 == 3) or (4 == 4.0)

"""## if,elif, else Statements"""

if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')

if 1 < 2:
    print('first')
else:
    print('last')

if 1 > 2:
    print('first')
else:
    print('last')

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

brand= "polo"
price = 1000
if brand == "polo":
  print("You have got a nice brand")
elif price == 1200:
  print("Price is reasonable")
else:
  print("You are out of brand and cash")

"""## for Loops"""

seq = [1,2,3,4,5]

for item in seq:
    print(item)

for item in seq:
    print('Yep')

for jelly in seq:
    print(jelly+jelly)

"""## while Loops"""

i = 1
while i < 10:
    print('i is: {}'.format(i))
    i = i+1

"""## range()"""

range(5)

range(1,10)

for i in range(5):
    print(i)

for i in range(1,10):
  print(i)

list(range(5))

tuple(range(10))

"""## list comprehension"""

x = [1,2,3,4]

out = []
for item in x:
    out.append(item**2)
print(out)

[item**2 for item in x]

[3*i for i in x]

"""## functions"""

def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)

my_func

my_func()

my_func('new param')

my_func(param1='new param')

def square(x):
    return x**2

out = square(2)

print(out)

def sum_of_nums(num1, num2):
  new_num = num1 + num2
  return new_num

sum_of_nums(2,3)

"""## lambda expressions"""

def times2(var):
    return var*2

times2(2)

sqar = lambda var: var*2

print(sqar)

"""## map and filter"""

seq = [1,2,3,4,5]

map(times2,seq)

list(map(times2,seq))

list(map(lambda var: var*2,seq))

fil = filter(lambda item: item%2 == 0,seq)
fil

list(filter(lambda item: item%2 == 0,seq))

"""## methods"""

st = 'hello my name is Sam'

st.lower()

st.upper()

st.split()

tweet = 'Go Sports! #Sports'

tweet.split('#')

tweet.split('#')[1]

email = "muhammadhassan@gmail.com"
email.split('@')

email.split()

d

d.keys()

d.items()

lst = [1,2,3]

lst.pop()

lst

'x' in [1,2,3]

'x' in ['x','y','z']

"""# Great Job!

Completed 02/02/2023
"""

