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

