"""
Python Lambda Function Syntax
Syntax: lambda arguments: expression

This function can have any number of arguments but only one expression, which is evaluated and returned.
One is free to use lambda functions wherever function objects are required.
You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
It has various uses in particular fields of programming, besides other types of expressions in functions.

"""
x = lambda x: x + 5
print(x(5))

#now take two argument

x = lambda a, b : a * b
print(x(5, 6))

#Print even number from 0 to 20
even_20 = [num for num in range(21) if num%2==0]
print(even_20)
#Output : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Print all even number greater than 20
even_g_20 = [num for num in range(40) if num%2==0 if num >= 20]
print(even_g_20)
#output: [20, 22, 24, 26, 28, 30, 32, 34, 36, 38]