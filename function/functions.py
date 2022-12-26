""" What is a function?
    Set of code or script which is defined to perform certain task
    Advantage : code reuseablity
            code simplicity/readablity
            bug resolving  """ 
#defining a function with the key word def 
def function_name():
    print("body of function")
    print("body of function")
    print("body of function")
#Calling a function 
function_name()

#parameterless funcion
def greeting():
    print("Welcome")
greeting()

"""Parameters & Arguments
   - Parameters are expexted values given from user
   - Arguments are values that user supplies to function"""
def greet_user(user_name):
    name = user_name.upper()
    print(f"Welcome{name}")
greet_user("Hssan")

#Output: Welcome
#let have define a funciton which add two number
# def additon(num_1, num_2):
#     result = num_1 + num_2
#     return result

# first_add = additon(12, 55)
# first_add