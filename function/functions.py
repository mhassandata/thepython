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
            Nationality of Student : {gender},
            Email of Student : {email},
            Contact number of Student : {contact}
        <__________________________________________>
            """)
bio_data("Mohd", "Hassan", "Male", "Pakistani", "abc@gmail.com", "01234557")


#Key word arguments



#Output: Welcome
#let have define a funciton which add two number
# def additon(num_1, num_2):
#     result = num_1 + num_2
#     return result

# first_add = additon(12, 55)
# first_add