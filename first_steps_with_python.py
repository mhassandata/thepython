

print(2 + 3 + 9+5+6)

99 - 77

23.54 * -1432


100 / 7


100 // 7

100 % 7

2/6

((2 + 5) * (17 - 3))


# In[ ]:


4 **3


# In[ ]:


98/64


# In[ ]:


((2 + 5) * (17 - 3)) / (4 ** 3)


# As you might expect, operators like `/` and `*` take precedence over other operators like `+` and `-` as per mathematical conventions. You can use parentheses, i.e. `(` and `)`, to specify the order in which operations are performed.

# Python supports the following arithmetic operators:
# 
# | Operator   | Purpose           | Example     | Result    |
# |------------|-------------------|-------------|-----------|
# | `+`        | Addition          | `2 + 3`     | `5`       |
# | `-`        | Subtraction       | `3 - 2`     | `1`       |
# | `*`        | Multiplication    | `8 * 12`    | `96`      |
# | `/`        | Division          | `100 / 7`   | `14.28..` |
# | `//`       | Floor Division    | `100 // 7`  | `14`      |    
# | `%`        | Modulus/Remainder | `100 % 7`   | `2`       |
# | `**`       | Exponent          | `5 ** 3`    | `125`     |
# 
# 
# 

# #Task 
# The population of a town is 198568. Out of them 45312 are men and 35678 are women. Find the number of children in the town.

# 198568-45312-35678

# In[ ]:





# ## Solving multi-step problems using variables
# 
# Let's try solving the following word problem using Python: 
# 
# > A grocery store sells a bag of ice for $1.25 and makes a 20% profit. If it sells 500 bags of ice, how much total profit does it make?
# 
# We can list out the information provided and gradually convert the word problem into a mathematical expression that can be evaluated using Python. 
# 
# *Cost of ice bag ($)* = 1.25
# 
# *Profit margin* = 20% = .2
# 
# *Profit per bag ($)* = profit margin * cost of ice bag = .2 * 1.25
# 
# *No. of bags* = 500
# 
# *Total profit* = no. of bags * profit per bag = 500 * (.2 * 1.25)

# In[ ]:


500 * (.2 * 1.25)


# Thus, the grocery store makes a total profit of $125. While this is a reasonable way to solve a problem, it's not entirely clear by looking at the code cell what the numbers represent. We can give names to each of the numbers by creating Python *variables*.
# 
# > **Variables**: While working with a programming language such as Python, information is stored in *variables*. You can think of variables as containers for storing data. The data stored within a variable is called its *value*.

# In[ ]:


cost_of_ice_bag = 1.25


# In[ ]:


profit_margin = .2


# In[ ]:


number_of_bags = 500


# The variables `cost_of_ice_bag`, `profit_margin`, and `number_of_bags` now contain the information provided in the word problem. We can check the value of a variable by typing its name into a cell. We can combine variables using arithmetic operations to create other variables.
# 
# > **Code completion**: While typing the name of an existing variable in a code cell within Jupyter, just type the first few characters and press the `Tab` key to autocomplete the variable's name. Try typing `pro` in a code cell below and press `Tab` to autocomplete to `profit_margin`.

# In[ ]:


profit_margin


# In[ ]:


profit_per_bag = cost_of_ice_bag * profit_margin


# In[ ]:


profit_per_bag


# In[ ]:


total_profit = number_of_bags * profit_per_bag


# In[ ]:


total_profit


# If you try to view the value of a variable that has not been *defined*, i.e., given a value using the assignment statement `variable_name = value`, Python shows an error.

# net_profit =0

# In[ ]:


net_profit


# Storing and manipulating data using appropriately named variables is a great way to explain what your code does.
# 
# Let's display the result of the word problem using a friendly message. We can do this using the `print` *function*.
# 
# > **Functions**: A function is a reusable set of instructions. It takes one or more inputs, performs certain operations, and often returns an output. Python provides many in-built functions like `print` and also allows us to define our own functions.

# In[ ]:


print("The grocery store makes a total profit of $", total_profit)


# > **`print`**: The `print` function is used to display information. It takes one or more inputs, which can be text (within quotes, e.g., `"this is some text"`), numbers, variables, mathematical expressions, etc. We'll learn more about variables & functions in the next tutorial.
# 
# Creating a code cell for each variable or mathematical operation can get tedious. Fortunately, Jupyter allows you to write multiple lines of code within a single code cell. The result of the last line of code within the cell is displayed as the output. 
# 
# Let's rewrite the solution to our word problem within a single cell.

# In[ ]:


# Store input data in variables
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Perform the required calculations
profit_per_bag = cost_of_ice_bag * profit_margin
total_profit = number_of_bags * profit_per_bag

# Display the result
print("The grocery store makes a total profit of $", total_profit)


# Note that we're using the `#` character to add *comments* within our code. 
# 
# > **Comments**: Comments and blank lines are ignored during execution, but they are useful for providing information to humans (including yourself) about what the code does. Comments can be inline (at the end of some code), on a separate line, or even span multiple lines. 
# 
# Inline and single-line comments start with `#`, whereas multi-line comments begin and end with three quotes, i.e. `"""`. Here are some examples of code comments:

# In[ ]:


my_favorite_number = 1 # an inline comment


# In[ ]:


# This comment gets its own line
my_least_favorite_number = 3


# In[ ]:


'''This is a multi-line comment.
Write as little or as much as you'd like.

Comments are really helpful for people reading
your code, but try to keep them short & to-the-point.

Also, if you use good variable names, then your code is
often self explanatory, and you may not even need comments!
'''
a_neutral_number = 5
a_neutral_number


# ## Evaluating conditions using Python
# 
# Apart from arithmetic operations, Python also provides several operations for comparing numbers & variables.
# 
# | Operator    | Description                                                     |
# |-------------|-----------------------------------------------------------------|
# | `==`        | Check if operands are equal                                     |
# | `!=`        | Check if operands are not equal                                 |
# | `>`         | Check if left operand is greater than right operand             |
# | `<`         | Check if left operand is less than right operand                |
# | `>=`        | Check if left operand is greater than or equal to right operand |
# | `<=`        | Check if left operand is less than or equal to right operand    |
# 
# The result of a comparison operation is either `True` or `False` (note the uppercase `T` and `F`). These are special keywords in Python. Let's try out some experiments with comparison operators.

# In[ ]:


my_favorite_number = 1
my_least_favorite_number = 5
a_neutral_number = 3


# In[ ]:


# Equality check - True
my_favorite_number == 2


# In[ ]:


# Equality check - False
my_favorite_number == my_least_favorite_number


# In[ ]:


# Not equal check - True
my_favorite_number == a_neutral_number


# In[ ]:


# Not equal check - False
a_neutral_number != 3


# In[ ]:


# Greater than check - True
my_least_favorite_number > a_neutral_number


# In[ ]:


# Greater than check - False
my_favorite_number > my_least_favorite_number


# In[ ]:


# Less than check - True
my_favorite_number < 10


# In[ ]:


# Less than check - False
my_least_favorite_number < my_favorite_number


# In[ ]:


# Greater than or equal check - True
my_favorite_number >= 1


# In[ ]:


# Greater than or equal check - False
my_favorite_number >= 3


# In[ ]:


# Less than or equal check - True
3 + 6 <= 9


# In[ ]:


# Less than or equal check - False
my_favorite_number + a_neutral_number <= 3


# Just like arithmetic operations, the result of a comparison operation can also be stored in a variable.

# In[ ]:


cost_of_ice_bag = 1.25
is_ice_bag_expensive = cost_of_ice_bag <= 10
print("Is the ice bag expensive?", is_ice_bag_expensive)


# ## Combining conditions with logical operators
# 
# The logical operators `and`, `or` and `not` operate upon conditions and `True` & `False` values (also known as *booleans*). `and` and `or` operate on two conditions, whereas `not` operates on a single condition.
# 
# The `and` operator returns `True` when both the conditions evaluate to `True`. Otherwise, it returns `False`.
# 
# | `a`     | `b`    | `a and b` |
# |---------|--------|-----------|
# |  `True` | `True` | `True`    |
# |  `True` | `False`| `False`   |
# |  `False`| `True` | `False`   |
# |  `False`| `False`| `False`   |
# 

# In[ ]:


my_favorite_number=1


# In[ ]:


my_favorite_number > 0 and my_favorite_number <= 3


# In[ ]:


my_favorite_number < 0 and my_favorite_number <= 3


# In[ ]:


my_favorite_number > 0 and my_favorite_number >= 3


# In[ ]:


True and False


# In[ ]:


True and True


# The `or` operator returns `True` if at least one of the conditions evaluates to `True`. It returns `False` only if both conditions are `False`.
# 
# | `a`     | `b`    | `a or b`  |
# |---------|--------|-----------|
# |  `True` | `True` | `True`    |
# |  `True` | `False`| `True`    |
# |  `False`| `True` | `True`    |
# |  `False`| `False`| `False`   |
# 
# 

# In[ ]:


a_neutral_number = 3


# In[ ]:


a_neutral_number == 3 or my_favorite_number < 0


# In[ ]:


a_neutral_number != 3 or my_favorite_number < 0


# In[ ]:


my_favorite_number < 0 or True


# In[ ]:


False or False


# The `not` operator returns `False` if a condition is `True` and `True` if the condition is `False`.

# In[ ]:


not a_neutral_number == 3


# In[ ]:


not my_favorite_number < 0


# In[ ]:


not False


# In[ ]:


not True


# Logical operators can be combined to form complex conditions. Use round brackets or parentheses `(` and `)` to indicate the order in which logical operators should be applied.

# In[ ]:


(2 > 3 and 4 <= 5) or not (my_favorite_number < 0 and True)


# In[ ]:


not (True and 0 < 1) or (False and True)


# If parentheses are not used, logical operators are applied from left to right.

# In[ ]:


not True and 0 < 1 or False and True


# Experiment with arithmetic, conditional and logical operators in Python using the interactive nature of Jupyter notebooks. We will learn more about variables and functions in future tutorials.

# ## Questions
# 
# 
# 1. What is the difference between the `/` and the `//` operators?
# 2. What is the difference between the `*` and the `**` operators?
# 3. What is the order of precedence for arithmetic operators in Python?
# 4. How do you specify the order in which arithmetic operations are performed in an expression involving multiple operators?
# 12. How do you solve a multi-step arithmetic word problem using Python?
# 13. What are variables? Why are they useful?
# 14. How do you create a variable in Python?
# 15. What is the assignment operator in Python?
# 16. What are the rules for naming a variable in Python?
# 17. How do you view the value of a variable?
# 18. How do you store the result of an arithmetic expression in a variable?
# 19. What happens if you try to access a variable that has not been defined?
# 20. How do you display messages in Python?
# 21. What types of inputs can the print function accept?
# 22. What are code comments? How are they useful?
# 23. What are the different ways of creating comments in Python code?
# 24. What are the different comparison operations supported in Python?
# 25. What is the result of a comparison operation?
# 26. What is the difference between `=` and `==` in Python?
# 27. What are the logical operators supported in Python?
# 28. What is the difference between the `and` and `or` operators?
# 29. Can you use comparison and logical operators in the same expression?
# 30. What is the purpose of using parentheses in arithmetic or logical expressions?
# 
# 
# 
