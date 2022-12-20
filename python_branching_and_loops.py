#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/Masadn/python-course/blob/main/python_branching_and_loops.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Python input()
# The input() method reads a line from input, converts into a string and returns it.
# 
# The syntax of input() method is:
# 
# input([prompt])
# 
# input() Parameters
# The input() method takes a single optional argument:
# 
# prompt (Optional) - a string that is written to standard output (usually screen) without trailing newline
# Return value from input()
# The input() method reads a line from the input (usually from the user), converts the line into a string by removing the trailing newline, and returns it.
# 
# ## How input() works in Python?
# 

# In[8]:


# How input() works in Python?
inputString = input()

print('The inputted string is:', inputString)


# # Convert User Input to a Number
# The input() function parse user input as a string even if it contains only digits.
# 

# In[10]:


data=input("Enter a Value: ")
type(data)


# How do we ensure a numeric input from the user? Most common alternative is to parse return value of the input() function to integer with int() function

# In[15]:


str_data=input("Enter a Number: ")
data=int(str_data)
print("str_data ",type(str_data))
print("data ",type(data))


# However, this is prone to error. If the user inputs non-numeric data, ValueError is raised.
# 

# In[16]:


data=int(input("Enter a Number: "))
type(data)


# # Task 
# Take two inputs from the user print out their Product.

# # Branching using Conditional Statements and Loops in Python
# 
# ![](https://i.imgur.com/7RfcHV0.png)
# 
# 
# 
# 

# This tutorial covers the following topics:
# 
# - Branching with `if`, `else` and `elif`
# - Nested conditions and `if` expressions
# - Iteration with `while` loops
# - Iterating over containers with `for` loops
# - Nested loops, `break` and `continue` statements

# ## Branching with `if`, `else` and `elif`
# 
# One of the most powerful features of programming languages is *branching*: the ability to make decisions and execute a different set of statements based on whether one or more conditions are true.
# 
# ### The `if` statement
# 
# In Python, branching is implemented using the `if` statement, which is written as follows:
# 
# ```
# if condition:
#     statement1
#     statement2
# ```
# 
# The `condition` can be a value, variable or expression. If the condition evaluates to `True`, then the statements within the *`if` block* are executed. Notice the four spaces before `statement1`, `statement2`, etc. The spaces inform Python that these statements are associated with the `if` statement above. This technique of structuring code by adding spaces is called *indentation*.
# 
# > **Indentation**: Python relies heavily on *indentation* (white space before a statement) to define code structure. This makes Python code easy to read and understand. You can run into problems if you don't use indentation properly. Indent your code by placing the cursor at the start of the line and pressing the `Tab` key once to add 4 spaces. Pressing `Tab` again will indent the code further by 4 more spaces, and press `Shift+Tab` will reduce the indentation by 4 spaces. 
# 
# 
# For example, let's write some code to check and print a message if a given number is even.

# In[ ]:


a_number = 34


# In[ ]:


if a_number % 2 == 0:
    print("We're inside an if block")
    print('The given number {} is even.'.format(a_number))


# We use the modulus operator `%` to calculate the remainder from the division of `a_number` by `2`. Then, we use the comparison operator `==` check if the remainder is `0`, which tells us whether the number is even, i.e., divisible by 2.
# 
# Since `34` is divisible by `2`, the expression `a_number % 2 == 0` evaluates to `True`, so the `print` statement under the `if` statement is executed. Also, note that we are using the string `format` method to include the number within the message.
# 
# Let's try the above again with an odd number.

# In[ ]:


another_number = 33


# In[ ]:


if another_number % 2 == 0:
    print('The given number {} is even.'.format(a_number))


# As expected, since the condition `another_number % 2 == 0` evaluates to `False`, no message is printed. 
# 
# ### The `else` statement
# 
# We may want to print a different message if the number is not even in the above example. This can be done by adding the `else` statement. It is written as follows:
# 
# ```
# if condition:
#     statement1
#     statement2
# else:
#     statement4
#     statement5
# 
# ```
# 
# If `condition` evaluates to `True`, the statements in the `if` block are executed. If it evaluates to `False`, the statements in the `else` block are executed.

# In[ ]:


a_number = 34


# In[ ]:


if a_number % 2 == 0:
    print('The given number {} is even.'.format(a_number))
else:
    print('The given number {} is odd.'.format(a_number))


# In[ ]:


another_number = 33


# In[ ]:


if another_number % 2 == 0:
    print('The given number {} is even.'.format(another_number))
else:
    print('The given number {} is odd.'.format(another_number))


# Here's another example, which uses the `in` operator to check membership within a tuple.

# In[ ]:


the_3_musketeers = ('Athos', 'Porthos', 'Aramis')


# In[ ]:


a_candidate = "D'Artagnan"


# In[ ]:


if a_candidate in the_3_musketeers:
    print("{} is a musketeer".format(a_candidate))
else:
    print("{} is not a musketeer".format(a_candidate))


# # Task 
# Write a program to check whether a person is eligible for voting or not.(voting age >=18)

# ### The `elif` statement
# 
# Python also provides an `elif` statement (short for "else if") to chain a series of conditional blocks. The conditions are evaluated one by one. For the first condition that evaluates to `True`, the block of statements below it is executed. The remaining conditions and statements are not evaluated. So, in an `if`, `elif`, `elif`... chain, at most one block of statements is executed, the one corresponding to the first condition that evaluates to `True`. 

# In[ ]:


today = 'Wednesday'


# In[ ]:


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


# In the above example, the first 3 conditions evaluate to `False`, so none of the first 3 messages are printed. The fourth condition evaluates to `True`, so the corresponding message is printed. The remaining conditions are skipped. Try changing the value of `today` above and re-executing the cells to print all the different messages.
# 
# 
# To verify that the remaining conditions are skipped, let us try another example.

# In[ ]:


a_number = 15


# In[ ]:


if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
elif a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
elif a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
elif a_number % 7 == 0:
    print('{} is divisible by 7'.format(a_number))


# Note that the message `15 is divisible by 5` is not printed because the condition `a_number % 5 == 0` isn't evaluated, since the previous condition `a_number % 3 == 0` evaluates to `True`. This is the key difference between using a chain of `if`, `elif`, `elif`... statements vs. a chain of `if` statements, where each condition is evaluated independently.

# In[ ]:


if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
if a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
if a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
if a_number % 7 == 0:
    print('{} is divisible by 7'.format(a_number))


# ### Using `if`, `elif`, and `else` together
# 
# You can also include an `else` statement at the end of a chain of `if`, `elif`... statements. This code within the `else` block is evaluated when none of the conditions hold true.

# In[ ]:


a_number = 49


# In[ ]:


if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
elif a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
elif a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
else:
    print('All checks failed!')
    print('{} is not divisible by 2, 3 or 5'.format(a_number))


# #Task 
# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
#     
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                                     10%
#         <= 50000                                                  5%

# Conditions can also be combined using the logical operators `and`, `or` and `not`. 

# In[ ]:


a_number = 12


# In[ ]:


if a_number % 3 == 0 and a_number % 5 == 0:
    print("The number {} is divisible by 3 and 5".format(a_number))
elif not a_number % 5 == 0:
    print("The number {} is not divisible by 5".format(a_number))


# ### Shorthand `if` conditional expression
# 
# A frequent use case of the `if` statement involves testing a condition and setting a variable's value based on the condition.

# In[ ]:


a_number = 13

if a_number % 2 == 0:
    parity = 'even'
else:
    parity = 'odd'

print('The number {} is {}.'.format(a_number, parity))


# Python provides a shorter syntax, which allows writing such conditions in a single line of code. It is known as a *conditional expression*, sometimes also referred to as a *ternary operator*. It has the following syntax:
# 
# ```
# x = true_value if condition else false_value
# ```
# 
# It has the same behavior as the following `if`-`else` block:
# 
# ```
# if condition:
#     x = true_value
# else:
#     x = false_value
# ```
# 
# Let's try it out for the example above.

# In[ ]:


parity = 'even' if a_number % 2 == 0 else 'odd'


# In[ ]:


print('The number {} is {}.'.format(a_number, parity))


# ### The `pass` statement
# 
# `if` statements cannot be empty, there must be at least one statement in every `if` and `elif` block. You can use the `pass` statement to do nothing and avoid getting an error.

# In[ ]:


a_number = 9


# In[ ]:


if a_number % 2 == 0:
elif a_number % 3 == 0:
    print('{} is divisible by 3 but not divisible by 2')


# In[ ]:


if a_number % 2 == 0:
    pass
elif a_number % 3 == 0:
    print('{} is divisible by 3 but not divisible by 2'.format(a_number))


# ## Iteration with `while` loops
# 
# Another powerful feature of programming languages, closely related to branching, is running one or more statements multiple times. This feature is often referred to as *iteration* on *looping*, and there are two ways to do this in Python: using `while` loops and `for` loops. 
# 
# `while` loops have the following syntax:
# 
# ```
# while condition:
#     statement(s)
# ```
# 
# Statements in the code block under `while` are executed repeatedly as long as the `condition` evaluates to `True`. Generally, one of the statements under `while` makes some change to a variable that causes the condition to evaluate to `False` after a certain number of iterations.
# 
# Let's try to calculate the factorial of `100` using a `while` loop. The factorial of a number `n` is the product (multiplication) of all the numbers from `1` to `n`, i.e., `1*2*3*...*(n-2)*(n-1)*n`.

# In[ ]:


result = 1
i = 1

while i <= 100:
    result = result * i
    i = i+1

print('The factorial of 100 is: {}'.format(result))


# Here's how the above code works:
# 
# * We initialize two variables, `result` and, `i`. `result` will contain the final outcome. And `i` is used to keep track of the next number to be multiplied with `result`. Both are initialized to 1 (can you explain why?)
# 
# * The condition `i <= 100` holds true (since `i` is initially `1`), so the `while` block is executed.
# 
# * The `result` is updated to `result * i`, `i` is increased by `1` and it now has the value `2`.
# 
# * At this point, the condition `i <= 100` is evaluated again. Since it continues to hold true, `result` is again updated to `result * i`, and `i` is increased to `3`.
# 
# * This process is repeated till the condition becomes false, which happens when `i` holds the value `101`. Once the condition evaluates to `False`, the execution of the loop ends, and the `print` statement below it is executed. 
# 
# Can you see why `result` contains the value of the factorial of 100 at the end? If not, try adding `print` statements inside the `while` block to print `result` and `i` in each iteration.
# 
# 
# > Iteration is a powerful technique because it gives computers a massive advantage over human beings in performing thousands or even millions of repetitive operations really fast. With just 4-5 lines of code, we were able to multiply 100 numbers almost instantly. The same code can be used to multiply a thousand numbers (just change the condition to `i <= 1000`) in a few seconds.
# 
# You can check how long a cell takes to execute by adding the *magic* command `%%time` at the top of a cell. Try checking how long it takes to compute the factorial of `100`, `1000`, `10000`, `100000`, etc. 

# In[ ]:


get_ipython().run_cell_magic('time', '', '\nresult = 1\ni = 1\n\nwhile i <= 1000:\n    result *= i # same as result = result * i\n    i += 1 # same as i = i+1\n\nprint(result)')


# Here's another example that uses two `while` loops to create an interesting pattern.

# ### Infinite Loops
# 
# Suppose the condition in a `while` loop always holds true. In that case, Python repeatedly executes the code within the loop forever, and the execution of the code never completes. This situation is called an infinite loop. It generally indicates that you've made a mistake in your code. For example, you may have provided the wrong condition or forgotten to update a variable within the loop, eventually falsifying the condition.
# 
# If your code is *stuck* in an infinite loop during execution, just press the "Stop" button on the toolbar (next to "Run") or select "Kernel > Interrupt" from the menu bar. This will *interrupt* the execution of the code. The following two cells both lead to infinite loops and need to be interrupted.

# In[1]:


# INFINITE LOOP - INTERRUPT THIS CELL

result = 1
i = 1

while i <= 100:
    result = result * i
    
    # forgot to increment i


# In[3]:


# INFINITE LOOP - INTERRUPT THIS CELL

result = 1
i = 1

while i > 0 : # wrong condition
    result *= i
    i += 1


# ### `break` and `continue` statements
# 
# You can use the `break` statement within the loop's body to immediately stop the execution and *break* out of the loop (even if the condition provided to `while` still holds true).

# In[ ]:


i = 1
result = 1

while i <= 100:
    result *= i
    if i == 42:
        print('Magic number 42 reached! Stopping execution..')
        break
    i += 1
    
print('i:', i)
print('result:', result)


# ## Iteration with `for` loops
# 
# A `for` loop is used for iterating or looping over sequences, i.e., lists, tuples, dictionaries, strings, and *ranges*. For loops have the following syntax:
# 
# ```
# for value in sequence:
#     statement(s)
# ```
# 
# The statements within the loop are executed once for each element in `sequence`. Here's an example that prints all the element of a list.

# In[ ]:


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in days:
    print(day)


# Let's try using `for` loops with some other data types.

# In[ ]:


# Looping over a string
for char in 'Monday':
    print(char)


# In[ ]:


# Looping over a tuple
for fruit in ['Apple', 'Banana', 'Guava']:
    print("Here's a fruit:", fruit)


# In[ ]:


# Looping over a dictionary
person = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}

for key in person:
    print("Key:", key, ",", "Value:", person[key])


# Note that while using a dictionary with a `for` loop, the iteration happens over the dictionary's keys. The key can be used within the loop to access the value. You can also iterate directly over the values using the `.values` method or over key-value pairs using the `.items` method.

# In[ ]:


for value in person.values():
    print(value)


# In[ ]:


for key_value_pair in person.items():
    print(key_value_pair)


# Since a key-value pair is a tuple, we can also extract the key & value into separate variables.

# In[ ]:


for key, value in person.items():
    print("Key:", key, ",", "Value:", value)


# ### Iterating using `range` and `enumerate`
# 
# The `range` function is used to create a sequence of numbers that can be iterated over using a `for` loop. It can be used in 3 ways:
#  
# * `range(n)` - Creates a sequence of numbers from `0` to `n-1`
# * `range(a, b)` - Creates a sequence of numbers from `a` to `b-1`
# * `range(a, b, step)` - Creates a sequence of numbers from `a` to `b-1` with increments of `step`
# 
# Let's try it out.

# In[ ]:


for i in range(7):
    print(i)


# In[ ]:


for i in range(3, 10):
    print(i)


# In[ ]:


for i in range(3, 14, 4):
    print(i)


# Ranges are used for iterating over lists when you need to track the index of elements while iterating.

# In[ ]:


a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(len(a_list)):
    print('The value at position {} is {}.'.format(i, a_list[i]))


# Another way to achieve the same result is by using the `enumerate` function with `a_list` as an input, which returns a tuple containing the index and the corresponding element.

# In[ ]:


for i, val in enumerate(a_list):
    print('The value at position {} is {}.'.format(i, val))


# ### `break`, `continue` and `pass` statements
# 
# Similar to `while` loops, `for` loops also support the `break` and `continue` statements. `break` is used for breaking out of the loop and `continue` is used for skipping ahead to the next iteration.

# In[ ]:


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


# In[ ]:


for day in weekdays:
    print('Today is {}'.format(day))
    if (day == 'Wednesday'):
        print("I don't work beyond Wednesday!")
        break


# In[ ]:


for day in weekdays:
    if (day == 'Wednesday'):
        print("I don't work on Wednesday!")
        continue
    print('Today is {}'.format(day))


# Like `if` statements, `for` loops cannot be empty, so you can use a `pass` statement if you don't want to execute any statements inside the loop.

# In[ ]:


for day in weekdays:
    pass


# ### Nested `for` and `while` loops
# 
# Similar to conditional statements, loops can be nested inside other loops. This is useful for looping lists of lists, dictionaries etc.

# In[ ]:


persons = [{'name': 'John', 'sex': 'Male'}, {'name': 'Jane', 'sex': 'Female'}]

for person in persons:
    for key in person:
        print(key, ":", person[key])
    print(" ")


# In[ ]:


days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['apple', 'banana', 'guava']

for day in days:
    for fruit in fruits:
        print(day, fruit)


# ## Questions for Revision
# 
# Try answering the following questions to test your understanding of the topics covered in this notebook:
# 
# 1. What is branching in programming languages?
# 2. What is the purpose of the `if` statement in Python?
# 3. What is the syntax of the `if` statement? Give an example.
# 4. What is indentation? Why is it used?
# 5. What is an indented block of statements?
# 6. How do you perform indentation in Python?
# 7. What happens if some code is not indented correctly?
# 8. What happens when the condition within the `if` statement evaluates to `True`? What happens if the condition evaluates for `false`?
# 9. How do you check if a number is even?
# 10. What is the purpose of the `else` statement in Python?
# 11. What is the syntax of the `else` statement? Give an example.
# 12. Write a program that prints different messages based on whether a number is positive or negative.
# 13. Can the `else` statement be used without an `if` statement?
# 14. What is the purpose of the `elif` statement in Python?
# 15. What is the syntax of the `elif` statement? Give an example.
# 16. Write a program that prints different messages for different months of the year.
# 17. Write a program that uses `if`, `elif`, and `else` statements together.
# 18. Can the `elif` statement be used without an `if` statement?
# 19. Can the `elif` statement be used without an `else` statement?
# 20. What is the difference between a chain of `if`, `elif`, `elif`… statements and a chain of `if`, `if`, `if`… statements? Give an example.
# 21. Can non-boolean conditions be used with `if` statements? Give some examples.
# 22. What are nested conditional statements? How are they useful?
# 23. Give an example of nested conditional statements.
# 24. Why is it advisable to avoid nested conditional statements?
# 25. What is the shorthand `if` conditional expression? 
# 26. What is the syntax of the shorthand `if` conditional expression? Give an example.
# 27. What is the difference between the shorthand `if` expression and the regular `if` statement?
# 28. What is a statement in Python?
# 29. What is an expression in Python?
# 30. What is the difference between statements and expressions?
# 31. Is every statement an expression? Give an example or counterexample.
# 32. Is every expression a statement? Give an example or counterexample.
# 33. What is the purpose of the pass statement in `if` blocks?
# 34. What is iteration or looping in programming languages? Why is it useful?
# 35. What are the two ways for performing iteration in Python?
# 36. What is the purpose of the `while` statement in Python?
# 37. What is the syntax of the `white` statement in Python? Give an example.
# 38. Write a program to compute the sum of the numbers 1 to 100 using a while loop. 
# 39. Repeat the above program for numbers up to 1000, 10000, and 100000. How long does it take each loop to complete?
# 40. What is an infinite loop?
# 41. What causes a program to enter an infinite loop?
# 42. How do you interrupt an infinite loop within Jupyter?
# 43. What is the purpose of the `break` statement in Python? 
# 44. Give an example of using a `break` statement within a while loop.
# 45. What is the purpose of the `continue` statement in Python?
# 46. Give an example of using the `continue` statement within a while loop.
# 47. What is logging? How is it useful?
# 48. What is the purpose of the `for` statement in Python?
# 49. What is the syntax of `for` loops? Give an example.
# 50. How are for loops and while loops different?
# 51. How do you loop over a string? Give an example.
# 52. How do you loop over a list? Give an example.
# 53. How do you loop over a tuple? Give an example.
# 54. How do you loop over a dictionary? Give an example.
# 55. What is the purpose of the `range` statement? Give an example.
# 56. What is the purpose of the `enumerate` statement? Give an example.
# 57. How are the `break`, `continue`, and `pass` statements used in for loops? Give examples.
# 
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




