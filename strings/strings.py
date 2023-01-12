""""
STRINGS
A string in Python is a sequence of characters
String can be enclosed by either double or single quotes

"""

my_string = "Hello, Python"
print(my_string)


#you can concatenate the string by + sign
first_name = "Mohd"
second_name = "Hassan"
full_name = first_name + second_name
print(full_name)


#You can split sentence by split method 
sentence = "My name is Mohd Hassan"
word = sentence.split()
print(word)
#Output: ['My', 'name', 'is', 'Mohd', 'Hassan']

#You can split the email by using split method
my_email = "mhassan@gmail.com"
name = my_email.split('@')
print(name)
#Output: ['mhassan', 'gmail.com']