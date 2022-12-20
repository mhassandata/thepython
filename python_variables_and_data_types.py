#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/Masadn/python-course/blob/main/python_variables_and_data_types.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # A Quick Tour of Variables and Data Types in Python
# 
# ![](https://i.imgur.com/6cg2E9Q.png)
# 
# 

# This tutorial covers the following topics:
# 
# - Storing information using variables
# - Primitive data types in Python: Integer, Float, Boolean, None and String
# - Built-in data structures in Python: List, Tuple and Dictionary
# - Methods and operators supported by built-in data types

# In[1]:



my_favorite_color = "blue"


# In[2]:


my_favorite_color


# A variable is created using an assignment statement. It begins with the variable's name, followed by the assignment operator `=` followed by the value to be stored within the variable.  Note that the assignment operator `=` is different from the equality comparison operator `==`.
# 
# You can also assign values to multiple variables in a single statement by separating the variable names and values with commas.

# In[3]:


color1, color2, color3 = "red", "green", "blue"


# In[4]:


color1


# In[5]:


color2


# In[6]:


color3


# You can assign the same value to multiple variables by chaining multiple assignment operations within a single statement.

# In[7]:


color4 = color5 = color6 = "magenta"


# In[8]:


color4


# In[9]:


color5


# In[10]:


color6


# You can change the value stored within a variable by assigning a new value to it using another assignment statement. Be careful while reassigning variables: when you assign a new value to the variable, the old value is lost and no longer accessible.

# In[11]:


my_favorite_color = "red"


# In[12]:


my_favorite_color


# While reassigning a variable, you can also use the variable's previous value to compute the new value.

# In[13]:


counter = 10


# In[14]:


counter


# In[15]:


counter = + 1


# In[16]:


counter


# The pattern `var = var op something` (where `op` is an arithmetic operator like `+`, `-`, `*`, `/`) is very common, so Python provides a *shorthand* syntax for it.

# In[17]:


counter = 10


# In[18]:


# Same as `counter = counter + 4`
counter += 4


# In[19]:


counter


# Variable names can be short (`a`, `x`, `y`, etc.) or descriptive ( `my_favorite_color`, `profit_margin`, `the_3_musketeers`, etc.). However, you must follow these rules while naming Python variables:
# 
# * A variable's name must start with a letter or the underscore character `_`. It cannot begin with a number.
# * A variable name can only contain lowercase (small) or uppercase (capital) letters, digits, or underscores (`a`-`z`, `A`-`Z`, `0`-`9`, and `_`).
# * Variable names are case-sensitive, i.e., `a_variable`, `A_Variable`, and `A_VARIABLE` are all different variables.
# 
# Here are some valid variable names:

# In[20]:


a_variable = 23
is_today_Saturday = False
my_favorite_car = "Delorean"
the_3_musketeers = ["Athos", "Porthos", "Aramis"] 


# Let's try creating some variables with invalid names. Python prints a syntax error if your variable's name is invalid.
# 
# > **Syntax**: The syntax of a programming language refers to the rules that govern the structure of a valid instruction or *statement*. If a statement does not follow these rules, Python stops execution and informs you that there is a *syntax error*. You can think of syntax as the rules of grammar for a programming language.

# In[21]:


a_ariable = 23


# In[22]:


is_today_aturday = False


# In[23]:


my_favorite_car = "Delorean"


# In[24]:


_3_musketeers = ["Athos", "Porthos", "Aramis"]


# ## Built-in data types in Python
# 
# Any data or information stored within a Python variable has a *type*. You can view the type of data stored within a variable using the `type` function.

# In[25]:


a_variable


# In[26]:


type(a_variable)


# In[27]:


is_today_Saturday


# In[28]:


type(is_today_Saturday)


# In[29]:


my_favorite_car


# In[30]:


type(my_favorite_car)


# In[31]:


the_3_musketeers


# In[32]:


type(the_3_musketeers)


# Python has several built-in data types for storing different kinds of information in variables. Following are some commonly used data types:
# 
# 1. Integer
# 2. Float
# 3. Boolean
# 4. None
# 5. String
# 6. List
# 7. Tuple
# 8. Dictionary
# 
# Integer, float, boolean, None, and string are *primitive data types* because they represent a single value. Other data types like list, tuple, and dictionary are often called *data structures* or *containers* because they hold multiple pieces of data together.

# ### Integer
# 
# Integers represent positive or negative whole numbers, from negative infinity to infinity. Note that integers should not include decimal points. Integers have the type `int`.

# In[33]:


current_year = 2021


# In[34]:


current_year


# In[35]:


type(current_year)


# Unlike some other programming languages, integers in Python can be arbitrarily large (or small). There's no lowest or highest value for integers, and there's just one `int` type (as opposed to `short`, `int`, `long`, `long long`, `unsigned int`, etc. in C/C++/Java).

# In[36]:


a_large_negative_number = -23374038374832934334234317348343


# In[37]:


a_large_negative_number


# In[38]:


type(a_large_negative_number)


# ### Float
# 
# Floats (or floating-point numbers) are numbers with a decimal point. There are no limits on the value or the number of digits before or after the decimal point. Floating-point numbers have the type `float`.

# In[39]:


pi = 3.141592653589793238


# In[40]:


pi


# In[41]:


type(pi)


# Note that a whole number is treated as a float if written with a decimal point, even though the decimal portion of the number is zero.

# In[42]:


a_number = 3.0


# In[43]:


a_number


# In[44]:


type(a_number)


# In[45]:


another_number = 4.


# In[46]:


another_number


# In[47]:


type(another_number)


# Floating point numbers can also be written using the scientific notation with an "e" to indicate the power of 10.

# In[48]:


one_hundredth = 1e-2


# In[49]:


one_hundredth


# In[50]:


type(one_hundredth)


# In[51]:


avogadro_number = 6.02214076e23


# In[52]:


avogadro_number


# In[53]:


type(avogadro_number)


# You can convert floats into integers and vice versa using the `float` and `int` functions. The operation of converting one type of value into another is called casting.

# In[54]:


float (current_year)


# In[55]:


float(a_large_negative_number)


# In[56]:


int(pi)


# In[57]:


int(avogadro_number)


# While performing arithmetic operations, integers are automatically converted to `float`s if any of the operands is a `float`. Also, the division operator `/` always returns a `float`, even if both operands are integers. Use the `//` operator if you want the result of the division to be an `int`.

# In[58]:


print(45*3.0)
type(45 * 3.0)


# In[59]:


type(45 * 3)


# In[60]:


type(10/3)


# In[61]:


type(10/2)


# In[62]:


type(10//2)


# ### Boolean
# 
# Booleans represent one of 2 values: `True` and `False`. Booleans have the type `bool`.

# In[63]:


is_today_Sunday = True


# In[64]:


is_today_Sunday


# In[65]:


type(is_today_Sunday)


# Booleans are generally the result of a comparison operation, e.g., `==`, `>=`, etc.

# In[66]:


cost_of_ice_bag = 1.25
is_ice_bag_expensive = cost_of_ice_bag >= 10


# In[67]:


is_ice_bag_expensive


# In[68]:


type(is_ice_bag_expensive)


# Booleans are automatically converted to `int`s when used in arithmetic operations. `True` is converted to `1` and `False` is converted to `0`.

# In[69]:


5 + False


# In[70]:


3. + True


# Any value in Python can be converted to a Boolean using the `bool` function. 
# 
# Only the following values evaluate to `False` (they are often called *falsy* values):
# 
# 1. The value `False` itself
# 2. The integer `0`
# 3. The float `0.0`
# 4. The empty value `None`
# 5. The empty text `""`
# 6. The empty list `[]`
# 7. The empty tuple `()`
# 8. The empty dictionary `{}`
# 9. The empty set `set()`
# 10. The empty range `range(0)`
# 
# Everything else evaluates to `True` (a value that evaluates to `True` is often called a *truthy* value).

# In[71]:


bool(False)


# In[72]:


bool(0)


# In[73]:


bool(0.0)


# In[74]:


bool(None)


# In[75]:


bool("")


# In[76]:


bool([])


# In[77]:


bool(())


# In[78]:


bool({})


# In[79]:


bool(set())


# In[80]:


bool(range(0))


# In[81]:


bool(True), bool(1), bool(2.0), bool("hello"), bool([1,2]), bool((2,3)), bool(range(10))


# ### None
# 
# The None type includes a single value `None`, used to indicate the absence of a value. `None` has the type `NoneType`. It is often used to declare a variable whose value may be assigned later.

# In[82]:


nothing = None


# In[83]:


type(nothing)


# ### String
# 
# A string is used to represent text (*a string of characters*) in Python. Strings must be surrounded using quotations (either the single quote `'` or the double quote `"`). Strings have the type `string`.

# In[84]:


today = "Saturday"


# In[85]:


today


# In[86]:


type(today)


# You can use single quotes inside a string written with double quotes, and vice versa.

# In[87]:


my_favorite_movie = "One Flew over the Cuckoo's Nest" 


# In[88]:


my_favorite_movie


# In[89]:


my_favorite_pun = 'Thanks for explaining the word "many" to me, it means a lot.'


# In[90]:


my_favorite_pun


# To use a double quote within a string written with double quotes, *escape* the inner quotes by prefixing them with the `\` character.

# In[91]:


another_pun = "The first time I got a universal remote control, I thought to myself \"This changes everything\"."


# In[92]:


another_pun


# Strings created using single or double quotes must begin and end on the same line. To create multiline strings, use three single quotes `'''` or three double quotes `"""` to begin and end the string. Line breaks are represented using the newline character `\n`.

# In[93]:


yet_another_pun = '''Son: "Dad, can you tell me what a solar eclipse is?" 
Dad: "No sun."'''


# In[94]:


yet_another_pun


# Multiline strings are best displayed using the `print` function.

# In[95]:


print(yet_another_pun)


# In[96]:


a_music_pun = """
Two windmills are standing in a field and one asks the other, 
"What kind of music do you like?"  

The other says, 
"I'm a big metal fan."
"""


# In[97]:


print(a_music_pun)


# You can check the length of a string using the `len` function.

# In[98]:


len(my_favorite_movie)


# Note that special characters like `\n` and escaped characters like `\"` count as a single character, even though they are written and sometimes printed as two characters.

# In[99]:


multiline_string = """a
b"""
multiline_string


# In[100]:


len(multiline_string)


# A string can be converted into a list of characters using `list` function.

# In[101]:


list(multiline_string)


# Strings also support several list operations, which are discussed in the next section. We'll look at a couple of examples here.
# 
# You can access individual characters within a string using the `[]` indexing notation. Note the character indices go from `0` to `n-1`, where `n` is the length of the string.

# In[102]:


today = "Saturday"


# In[103]:


today[0]


# In[104]:


today[3]


# In[105]:


today[7]


# You can access a part of a string using by providing a `start:end` range instead of a single index in `[]`.

# In[106]:


today[5:8]


# You can also check whether a string contains a some text using the `in` operator. 

# In[107]:


'day' in today


# In[108]:


'Sun' in today


# Two or more strings can be joined or *concatenated* using the `+` operator. Be careful while concatenating strings, sometimes you may need to add a space character `" "` between words.

# In[109]:


full_name = "Derek O'Brien"


# In[110]:


greeting = "Hello"


# In[111]:


greeting + full_name


# In[112]:


greeting + " " + full_name + "!" # additional space


# Strings in Python have many built-in *methods* that are used to manipulate them. Let's try out some common string methods.
# 
# > **Methods**: Methods are functions associated with data types and are accessed using the `.` notation e.g. `variable_name.method()` or `"a string".method()`. Methods are a powerful technique for associating common operations with values of specific data types.
# 
# The `.lower()`, `.upper()` and `.capitalize()` methods are used to change the case of the characters.

# In[113]:


today.lower()


# In[114]:


"saturday".upper()


# In[115]:


"monday".capitalize() # changes first character to uppercase


# The `.replace` method replaces a part of the string with another string. It takes the portion to be replaced and the replacement text as *inputs* or *arguments*.

# In[116]:


another_day = today.replace("Satur", "Wednes")


# In[117]:


another_day


# Note that `replace` returns a new string, and the original string is not modified.

# In[118]:


today


# The `.split` method splits a string into a list of strings at every occurrence of provided character(s).

# In[119]:


"Sun,Mon,Tue,Wed,Thu,Fri,Sat".split(",")


# The `.strip` method removes whitespace characters from the beginning and end of a string.

# In[120]:


a_long_line = "       This is a long line with some space before, after,     and some space in the middle..    "


# In[121]:


a_long_line_stripped = a_long_line.strip()


# In[122]:


a_long_line_stripped


# The `.format` method combines values of other data types, e.g., integers, floats, booleans, lists, etc. with strings. You can use `format` to construct output messages for display.

# In[123]:


# Input variables
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Template for output message
output_template = """If a grocery store sells ice bags at $ {} per bag, with a profit margin of {} %, 
then the total profit it makes by selling {} ice bags is $ {}."""

print(output_template)


# In[124]:


# Inserting values into the string
total_profit = cost_of_ice_bag * profit_margin * number_of_bags
output_message = output_template.format(cost_of_ice_bag, profit_margin*100, number_of_bags, total_profit)

print(output_message)


# Notice how the placeholders `{}` in the `output_template` string are replaced with the arguments provided to the `.format` method.
# 
# It is also possible to use the string concatenation operator `+` to combine strings with other values. However, those values must first be converted to strings using the `str` function.

# In[125]:


"If a grocery store sells ice bags at $ " + cost_of_ice_bag + ", with a profit margin of " + profit_margin


# In[ ]:


"If a grocery store sells ice bags at $ " + str(cost_of_ice_bag) + ", with a profit margin of " + str(profit_margin)


# You can `str` to convert a value of any data type into a string.

# In[ ]:


str(23)


# In[ ]:


str(23.432)


# In[ ]:


str(True)


# In[ ]:


the_3_musketeers = ["Athos", "Porthos", "Aramis"]
str(the_3_musketeers)


# Note that all string methods return new values and DO NOT change the existing string. You can find a full list of string methods here: https://www.w3schools.com/python/python_ref_string.asp. 

# Strings also support the comparison operators `==` and `!=` for checking whether two strings are equal.

# In[ ]:


first_name = "John"


# In[ ]:


first_name == "Doe"


# In[ ]:


first_name == "John"


# In[ ]:


first_name != "Jane"


# ### List
# 
# A list in Python is an ordered collection of values. Lists can hold values of different data types and support operations to add, remove, and change values. Lists have the type `list`.
# 
# To create a list, enclose a sequence of values within square brackets `[` and `]`, separated by commas.

# In[ ]:


fruits = ['apple', 'banana', 'cherry']


# In[ ]:


fruits


# In[ ]:


type(fruits)


# Let's try creating a list containing values of different data types, including another list.

# In[ ]:


a_list = [23, 'hello', None, 3.14, fruits, 3 <= 5]


# In[ ]:


a_list


# In[ ]:


empty_list = []


# In[ ]:


empty_list


# To determine the number of values in a list, use the `len` function. You can use `len`  to determine the number of values in several other data types.

# In[ ]:


len(fruits)


# In[ ]:


print("Number of fruits:", len(fruits))


# In[ ]:


len(a_list)


# In[ ]:


len(empty_list)


# You can access an element from the list using its *index*, e.g., `fruits[2]` returns the element at index 2 within the list `fruits`. The starting index of a list is 0.

# In[ ]:


fruits[0]


# In[ ]:


fruits[1]


# In[ ]:


fruits[2]


# If you try to access an index equal to or higher than the length of the list, Python returns an `IndexError`.

# In[ ]:


fruits[3]


# In[ ]:


fruits[4]


# You can use negative indices to access elements from the end of a list, e.g., `fruits[-1]` returns the last element, `fruits[-2]` returns the second last element, and so on.

# In[ ]:


fruits[-1]


# In[ ]:


fruits[-2]


# In[ ]:


fruits[-3]


# In[ ]:


fruits[-4]


# You can also access a range of values from the list. The result is itself a list. Let us look at some examples.

# In[ ]:


a_list = [23, 'hello', None, 3.14, fruits, 3 <= 5]


# In[ ]:


a_list


# In[ ]:


len(a_list)


# In[ ]:


a_list[2:5]


# Note that the range `2:5` includes the element at the start index `2` but does not include the element at the end index `5`. So, the result has 3 values (index `2`, `3`, and `4`).
# 
# Here are some experiments you should try out (use the empty cells below):
# 
# * Try setting one or both indices of the range are larger than the size of the list, e.g., `a_list[2:10]`
# * Try setting the start index of the range to be larger than the end index, e.g., `list_a[2:10]`
# * Try leaving out the start or end index of a range, e.g., `a_list[2:]` or `a_list[:5]`
# * Try using negative indices for the range, e.g., `a_list[-2:-5]` or `a_list[-5:-2]` (can you explain the results?)
# 
# > The flexible and interactive nature of Jupyter notebooks makes them an excellent tool for learning and experimentation. If you are new to Python, you can resolve most questions as soon as they arise simply by typing the code into a cell and executing it. Let your curiosity run wild, discover what Python is capable of and what it isn't! 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# You can also change the value at a specific index within a list using the assignment operation.

# In[ ]:


fruits


# In[ ]:


fruits[1] = 'blueberry'


# In[ ]:


fruits


# A new value can be added to the end of a list using the `append` method.

# In[ ]:


fruits.append('dates')


# In[ ]:


fruits


# A new value can also be inserted at a specific index using the `insert` method.

# In[ ]:


fruits.insert(1, 'banana')


# In[ ]:


fruits


# You can remove a value from a list using the `remove` method.

# In[ ]:


fruits.remove('blueberry')


# In[ ]:


fruits


# What happens if a list has multiple instances of the value passed to `.remove`? Try it out.

# In[ ]:





# In[ ]:





# To remove an element from a specific index, use the `pop` method. The method also returns the removed element.

# In[ ]:


fruits


# In[ ]:


fruits.pop(1)


# In[ ]:


fruits


# If no index is provided, the `pop` method removes the last element of the list.

# In[ ]:


fruits.pop()


# In[ ]:


fruits


# You can test whether a list contains a value using the `in` operator.

# In[ ]:


'pineapple' in fruits


# In[ ]:


'cherry' in fruits


# To combine two or more lists, use the `+` operator. This operation is also called *concatenation*.

# In[ ]:


fruits


# In[ ]:


more_fruits = fruits + ['pineapple', 'tomato', 'guava'] + ['dates', 'banana']


# In[ ]:


more_fruits


# To create a copy of a list, use the `copy` method. Modifying the copied list does not affect the original.

# In[ ]:


more_fruits_copy = more_fruits.copy()


# In[ ]:


more_fruits_copy


# In[ ]:


# Modify the copy
more_fruits_copy.remove('pineapple')
more_fruits_copy.pop()
more_fruits_copy


# In[ ]:


# Original list remains unchanged
more_fruits


# Note that you cannot create a copy of a list by simply creating a new variable using the assignment operator `=`. The new variable will point to the same list, and any modifications performed using either variable will affect the other.

# In[ ]:


more_fruits


# In[ ]:


more_fruits_not_a_copy = more_fruits


# In[ ]:


more_fruits_not_a_copy.remove('pineapple')
more_fruits_not_a_copy.pop()


# In[ ]:


more_fruits_not_a_copy


# In[ ]:


more_fruits


# Just like strings, there are several in-built methods to manipulate a list. However, unlike strings, most list methods modify the original list rather than returning a new one. Check out some common list operations here: https://www.w3schools.com/python/python_ref_list.asp .
# 
# 
# Following are some exercises you can try out with list methods (use the blank code cells below):
# 
# * Reverse the order of elements in a list
# * Add the elements of one list at the end of another list
# * Sort a list of strings in alphabetical order
# * Sort a list of numbers in decreasing order

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Tuple
# 
# A tuple is an ordered collection of values, similar to a list. However, it is not possible to add, remove, or modify values in a tuple. A tuple is created by enclosing values within parentheses `(` and `)`, separated by commas.
# 
# > Any data structure that cannot be modified after creation is called *immutable*. You can think of tuples as immutable lists.
# 
# Let's try some experiments with tuples.

# In[ ]:


fruits = ('apple', 'cherry', 'dates')


# In[ ]:


# check no. of elements
len(fruits)


# In[ ]:


# get an element (positive index)
fruits[0]


# In[ ]:


# get an element (negative index)
fruits[-2]


# In[ ]:


# check if it contains an element
'dates' in fruits


# In[ ]:


# try to change an element
fruits[0] = 'avocado'


# In[ ]:


# try to append an element
fruits.append('blueberry')


# In[ ]:


# try to remove an element
fruits.remove('apple')


# You can also skip the parantheses `(` and `)` while creating a tuple. Python automatically converts comma-separated values into a tuple.

# In[ ]:


the_3_musketeers = 'Athos', 'Porthos', 'Aramis'


# In[ ]:


the_3_musketeers


# You can also create a tuple with just one element by typing a comma after it. Just wrapping it with parentheses `(` and `)` won't make it a tuple.

# In[ ]:


single_element_tuple = 4,


# In[ ]:


single_element_tuple


# In[ ]:


another_single_element_tuple = (4,)


# In[ ]:


another_single_element_tuple


# In[ ]:


not_a_tuple = (4)


# In[ ]:


not_a_tuple


# Tuples are often used to create multiple variables with a single statement.

# In[ ]:


point = (3, 4)


# In[ ]:


point_x, point_y = point


# In[ ]:


point_x


# In[ ]:


point_y


# You can convert a list into a tuple using the `tuple` function, and vice versa using the `list` function

# In[ ]:


tuple(['one', 'two', 'three'])


# In[ ]:


list(('Athos', 'Porthos', 'Aramis'))


# Tuples have just two built-in methods: `count` and `index`. Can you figure out what they do? While you look could look for documentation and examples online, there's an easier way to check a method's documentation, using the `help` function.

# In[ ]:


a_tuple = 23, "hello", False, None, 23, 37, "hello"


# In[ ]:


help(a_tuple.count)


# Within a Jupyter notebook, you can also start a code cell with `?` and type the name of a function or method. When you execute this cell, you will see the function/method's documentation in a pop-up window.

# In[ ]:


get_ipython().run_line_magic('pinfo', 'a_tuple.index')


# Try using `count` and `index` with `a_tuple` in the code cells below.

# In[ ]:





# In[ ]:





# ### Dictionary
# 
# A dictionary is an unordered collection of items. Each item stored in a dictionary has a key and value. You can use a key to retrieve the corresponding value from the dictionary.  Dictionaries have the type `dict`.
# 
# Dictionaries are often used to store many pieces of information e.g. details about a person, in a single variable. Dictionaries are created by enclosing key-value pairs within braces or curly brackets `{` and `}`.

# In[ ]:


person1 = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}


# In[ ]:


person1


# Dictionaries can also be created using the `dict` function.

# In[ ]:


person2 = dict(name='Jane Judy', sex='Female', age=28, married=False)


# In[ ]:


person2


# In[ ]:


type(person1)


# Keys can be used to access values using square brackets `[` and `]`.

# In[ ]:


person1['name']


# In[ ]:


person1['married']


# In[ ]:


person2['name']


# If a key isn't present in the dictionary, then a `KeyError` is *thrown*.

# In[ ]:


person1['address']


# You can also use the `get` method to access the value associated with a key.

# In[ ]:


person2.get("name")


# The `get` method also accepts a default value, returned if the key is not present in the dictionary.

# In[ ]:


person2.get("address", "Unknown")


# You can check whether a key is present in a dictionary using the `in` operator.

# In[ ]:


'name' in person1


# In[ ]:


'address' in person1


# You can change the value associated with a key using the assignment operator.

# In[ ]:


person2['married']


# In[ ]:


person2['married'] = True


# In[ ]:


person2['married']


# The assignment operator can also be used to add new key-value pairs to the dictionary.

# In[ ]:


person1


# In[ ]:


person1['address'] = '1, Penny Lane'


# In[ ]:


person1


# To remove a key and the associated value from a dictionary, use the `pop` method.

# In[ ]:


person1.pop('address')


# In[ ]:


person1


# Dictionaries also provide methods to view the list of keys, values, or key-value pairs inside it.

# In[ ]:


person1.keys()


# In[ ]:


person1.values()


# In[ ]:


person1.items()


# In[ ]:


person1.items()[1]


# The results of `keys`, `values`, and `items` look like lists. However, they don't support the indexing operator `[]` for retrieving elements. 
# 
# Can you figure out how to access an element at a specific index from these results? Try it below. *Hint: Use the `list` function*

# In[ ]:





# In[ ]:





# Dictionaries provide many other methods. You can learn more about them here: https://www.w3schools.com/python/python_ref_dictionary.asp .
# 
# Here are some experiments you can try out with dictionaries (use the empty cells below):
# * What happens if you use the same key multiple times while creating a dictionary?
# * How can you create a copy of a dictionary (modifying the copy should not change the original)?
# * Can the value associated with a key itself be a dictionary?
# * How can you add the key-value pairs from one dictionary into another dictionary? Hint: See the `update` method.
# * Can the dictionary's keys be something other than a string, e.g., a number, boolean, list, etc.?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Questions for Revision
# 
# Try answering the following questions to test your understanding of the topics covered in this notebook:
# 
# 1. What is a variable in Python?
# 2. How do you create a variable?
# 3. How do you check the value within a variable?
# 4. How do you create multiple variables in a single statement?
# 5. How do you create multiple variables with the same value?
# 6. How do you change the value of a variable?
# 7. How do you reassign a variable by modifying the previous value?
# 8. What does the statement `counter += 4` do?
# 9. What are the rules for naming a variable?
# 10. Are variable names case-sensitive? Do `a_variable`, `A_Variable`, and `A_VARIABLE` represent the same variable or different ones?
# 11. What is Syntax? Why is it important?
# 12. What happens if you execute a statement with invalid syntax?
# 13. How do you check the data type of a variable?
# 14. What are the built-in data types in Python?
# 15. What is a primitive data type? 
# 16. What are the primitive data types available in Python?
# 17. What is a data structure or container data type?
# 18. What are the container types available in Python?
# 19. What kind of data does the Integer data type represent?
# 20. What are the numerical limits of the integer data type?
# 21. What kind of data does the float data type represent?
# 22. How does Python decide if a given number is a float or an integer?
# 23. How can you create a variable which stores a whole number, e.g., 4 but has the float data type?
# 24. How do you create floats representing very large (e.g., 6.023 x 10^23) or very small numbers (0.000000123)?
# 25. What does the expression `23e-12` represent?
# 26. Can floats be used to store numbers with unlimited precision?
# 27. What are the differences between integers and floats?
# 28. How do you convert an integer to a float?
# 29. How do you convert a float to an integer?
# 30. What is the result obtained when you convert 1.99 to an integer?
# 31. What are the data types of the results of the division operators `/` and `//`?
# 32. What kind of data does the Boolean data type represent?
# 33. Which types of Python operators return booleans as a result?
# 34. What happens if you try to use a boolean in arithmetic operation?
# 35. How can any value in Python be covered to a boolean?
# 36. What are truthy and falsy values?
# 37. What are the values in Python that evaluate to False?
# 38. Give some examples of values that evaluate to True.
# 39. What kind of data does the None data type represent?
# 40. What is the purpose of None?
# 41. What kind of data does the String data type represent?
# 42. What are the different ways of creating strings in Python?
# 43. What is the difference between strings creating using single quotes, i.e. `'` and `'` vs. those created using double quotes, i.e. `"` and `"`?
# 44. How do you create multi-line strings in Python?
# 45. What is the newline character, `\n`?
# 46. What are escaped characters? How are they useful?
# 47. How do you check the length of a string?
# 48. How do you convert a string into a list of characters?
# 49. How do you access a specific character from a string?
# 50. How do you access a range of characters from a string?
# 51. How do you check if a specific character occurs in a string?
# 52. How do you check if a smaller string occurs within a bigger string?
# 53. How do you join two or more strings?
# 54. What are "methods" in Python? How are they different from functions?
# 55. What do the `.lower`, `.upper` and `.capitalize` methods on strings do?
# 56. How do you replace a specific part of a string with something else?
# 57. How do you split the string "Sun,Mon,Tue,Wed,Thu,Fri,Sat" into a list of days?
# 58. How do you remove whitespace from the beginning and end of a string?
# 59. What is the string `.format` method used for? Can you give an example?
# 60. What are the benefits of using the `.format` method instead of string concatenation?
# 61. How do you convert a value of another type to a string?
# 62. How do you check if two strings have the same value?
# 63. Where can you find the list of all the methods supported by strings?
# 64. What is a list in Python?
# 65. How do you create a list?
# 66. Can a Python list contain values of different data types?
# 67. Can a list contain another list as an element within it?
# 68. Can you create a list without any values?
# 69. How do you check the length of a list in Python?
# 70. How do you retrieve a value from a list?
# 71. What is the smallest and largest index you can use to access elements from a list containing five elements?
# 72. What happens if you try to access an index equal to or larger than the size of a list?
# 73. What happens if you try to access a negative index within a list?
# 74. How do you access a range of elements from a list?
# 75. How many elements does the list returned by the expression `a_list[2:5]` contain?
# 76. What do the ranges `a_list[:2]` and `a_list[2:]` represent?
# 77. How do you change the item stored at a specific index within a list?
# 78. How do you insert a new item at the beginning, middle, or end of a list?
# 79. How do you remove an item from al list?
# 80. How do you remove the item at a given index from a list?
# 81. How do you check if a list contains a value?
# 82. How do you combine two or most lists to create a larger list?
# 83. How do you create a copy of a list?
# 84. Does the expression `a_new_list = a_list` create a copy of the list `a_list`?
# 85. Where can you find the list of all the methods supported by lists?
# 86. What is a Tuple in Python?
# 87. How is a tuple different from a list?
# 88. Can you add or remove elements in a tuple?
# 89. How do you create a tuple with just one element?
# 90. How do you convert a tuple to a list and vice versa?
# 91. What are the `count` and `index` method of a Tuple used for?
# 92. What is a dictionary in Python?
# 93. How do you create a dictionary?
# 94. What are keys and values?
# 95. How do you access the value associated with a specific key in a dictionary?
# 96. What happens if you try to access the value for a key that doesn't exist in a dictionary?
# 97. What is the `.get` method of a dictionary used for?
# 98. How do you change the value associated with a key in a dictionary?
# 99. How do you add or remove a key-value pair in a dictionary?
# 100. How do you access the keys, values, and key-value pairs within a dictionary?
# 

# In[ ]:




