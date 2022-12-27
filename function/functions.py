""" What is a function?
    Set of code or script which is defined to perform certain task
    Advantage : code reuseablity
            code simplicity/readablity
            bug resolving  """ 
""""Function Continue..
Define
Call
Parameters
Arguments
Return
Keyword Arguments

Default Parameters"""

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

def greet_user(user_name):  #parameter
    name = user_name.upper()
    print(f"Welcome {name}")
greet_user("Hassan")



#Now we will see the multiple parameters 

def bio_data(f_name, l_name, gender, nationality, email, contact):
    print(f""" 
        <__________________________________>
            First Name of Student : {f_name},
            Last name of Student : {l_name},
            Gender of Student : {gender},
            Nationality of Student : {nationality},
            Email of Student : {email},
            Contact number of Student : {contact}
        <__________________________________________>
            """)
bio_data("Mohd", "Hassan", "Male", "Pakistani", "abc@gmail.com", "01234557")


""""
Output will be like..
        <__________________________________>
            First Name of Student : Mohd,
            Last name of Student : Hassan,
            Gender of Student : Male,
            Nationality of Student : Pakistani,
            Email of Student : abc@gmail.com,
            Contact number of Student : 01234557
        <__________________________________________>
"""

#Key word arguments
def full_name(first_name, last_name, age):
    print(f"{first_name} {last_name}")
    print(f"Age is  : {age}")

full_name(age=27, last_name="Hassan", first_name="Mohd")

#let have define a funciton which add two number
def additon(num_1, num_2):
    result = num_1 + num_2
    return result

first_add = additon(12, 55)
print("Addition of num_1 and num_2 is = ", first_add)


#Let have calculate the area of triagles
def area_of_triagle(length, width):
    area = 0.5 * (length * width)
    return area

area_of_triagle_1 = area_of_triagle(4, 9)
print("Area of first triangle is = ", area_of_triagle_1)

#Same as above
def areaOfTriagle(l, w):
    area = 0.5 * l * w
    print(f"Area of triangle is = {area} sq.cm")
areaOfTriagle(4, 9)
# Output: Area of triangle is = 18.0 sq.cm


#Arbitrary number of arguments
def user_details(name, email, *others_details):
    print(name)
    print(email)
    for val in others_details:
        print(val)
user_details("Hassan", "abc@gmail.com", "mhassan", "ceo")

"""output: Hassan
abc@gmail.com
mhassan
ceo """

#If we are passing keyword-arguments 
def user_details1(name, email, **others_details1):
    print(name)
    print(email)
    for k, val in others_details1.items():
        print(k , val)
user_details1("Hassan", "abc@yahoo.com", city="gilgit", country="Pakistan")