#variable in pythonStoring information using variables
#Primitive data types in Python: Integer, Float, Boolean, None and String
#Built-in data structures in Python: List, Tuple and Dictionary
#Methods and operators supported by built-in data types

a = 12
b = 1
print(a + b)

my_favourite_color = "green"
print(my_favourite_color)


#Another method of declear variables
#A variable is created using an assignment statement. 
# It begins with the variable's name, followed by the assignment operator = followed by the value to be stored within the variable. 
# Note that the assignment operator = is different from the equality comparison operator ==.
#You can also assign values to multiple variables in a single statement by separating the variable names and values with commas.
col1, col2, col3 = "green", "red", "blue"
print(col1, col2, col3)

#You can assign the same value to multiple variables by chaining multiple assignment operations within a single statement.
col4 = col5 = col6 = "white"
print(col4)
print(col5)

#The pattern var = var op something (where op is an arithmetic operator like +, -, *, /) is very common, 
# so Python provides a shorthand syntax for it.
counter = 10
counter+= 1
print(counter)

################################################################################################################
'''Variable names can be short (a, x, y, etc.) or descriptive ( my_favorite_color, profit_margin, the_3_musketeers, etc.). However, you must follow these rules while naming Python variables:

A variable's name must start with a letter or the underscore character _. It cannot begin with a number.
A variable name can only contain lowercase (small) or uppercase (capital) letters, digits, or underscores (a-z, A-Z, 0-9, and _).
Variable names are case-sensitive, i.e., a_variable, A_Variable, and A_VARIABLE are all different variables.'''

#Here are some valid variable names:
a_variable = 23
is_today_Saturday = False
my_favorite_car = "Delorean"
the_3_musketeers = ["Athos", "Porthos", "Aramis"]

print(the_3_musketeers)



"""Python has several built-in data types for storing different kinds of information in variables. Following are some commonly used data types:
    1. Integer
    2. Float
    3. Boolean
    4. None
    5. String
    6. List
    7. Tuple
    8. Dictionary
Integer, float, boolean, None, and string are primitive data types because they represent a single value. Other data types like list, tuple, and dictionary are often called data structures or containers because they hold multiple pieces of data together.
"""
# 1. Integer
"""Integers represent positive or negative number """
my_favourite_num = 11
current_year = 2022
print(type(current_year))

num = -33
print(num)

#2. Float

"""Float
Floats (or floating-point numbers) are numbers with a decimal point. 
There are no limits on the value or the number of digits before or after the decimal point. 
Floating-point numbers have the type float."""

a_number = 3.0
print(type(a_number))

"""While performing arithmetic operations, integers are automatically converted to floats if any of the operands is a float. 
Also, the division operator / always returns a float, even if both operands are integers. 
Use the // operator if you want the result of the division to be an int."""

print(45*3.0)
type(45 * 3.0)

#3. Boolean
"""Boolean
Booleans represent one of 2 values: True and False. Booleans have the type bool."""

is_this_sunday = True
is_this_friday = False
print(is_this_sunday)
print(is_this_friday)


"""Any value in Python can be converted to a Boolean using the bool function.

Only the following values evaluate to False (they are often called falsy values):

    1. The value False itself
    2. The integer 0
    3. The float 0.0
    4. The empty value None
    5. The empty text ""
    6. The empty list []
    7. The empty tuple ()
    8. The empty dictionary {}
    9. The empty set set()
    10. The empty range range(0)
Everything else evaluates to True (a value that evaluates to True is often called a truthy value)."""
bool(True), bool(1), bool(2.0), bool("hello"), bool([1,2]), bool((2,3)), bool(range(10))
print(bool(True), bool(1), bool(2.0), bool("hello"), bool([1,2]), bool((2,3)), bool(range(10)))


# 4. None
"""The None type includes a single value None, used to indicate the absence of a value. None has the type NoneType. 
It is often used to declare a variable whose value may be assigned later."""

nothing = None
print(nothing)


# 5. String
"""A string is used to represent text (a string of characters) in Python. 
Strings must be surrounded using quotations (either the single quote ' or the double quote "). Strings have the type string."""

today = "Sunday"
my_favourite_movie = "the north"

#Strings created using single or double quotes must begin and end on the same line. To create multiline strings, use three single quotes ''' or three double quotes """ to begin and end the string. 
#Line breaks are represented using the newline character \n.

a_music_pun = """
Two windmills are standing in a field and one asks the other, 
"What kind of music do you like?"  

The other says, 
"I'm a big metal fan."
"""
print(a_music_pun)


#lets Creat a string variable and print its lucky number
my_lucky_number = "Hassan"
number = len(my_lucky_number) * 5
print("Hello {} your lucky number is {}".format(my_lucky_number, number))

#Output: Hello Hassan your lucky number is 30