""" What is a function?
    Set of code or script which is defined to perform certain task
    Advantage : code reuseablity
            code simplicity/readablity
            bug resolving  """ 
    #Functions can be used to quickly find information and perform calculations using specific values.
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

""""mhassan
ceo
Hassan
abc@yahoo.com
city gilgit
country Pakistan"""
#write a script to count file characters
with open("myfile.txt") as my_file:
    text = my_file.read()
    length = len(text)
print("The file is {} characters long.".format(length))
#output is : The file is 136 characters long.

#Now we will see the specific character repetition in the file.
n = 0
for word in text.split():
  if word.lower() in ['a', 'the']:
    n += 1
print('The file has "a" {} times'.format(n))
#output : The file has "a" 9 times


""""
Task. Album: Write a function called make_album() that builds a dictionary
describing a music album The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information Use the function to make three dictionaries representing different
albums Print each return value to show that the dictionaries are storing the
album information correctly
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album If the calling line includes a value for the number of tracks, add that value to the album’s dictionary Make at least one new
function call that includes the number of tracks on an album
"""
##one way to write a funciton
def make_album(artis_name, album_title):
    album = {}
    album["artist"] = artis_name
    album["title"] = album_title
    return album
### Calling function with object album1
album1 = make_album("Arjit Singn", "Pardas")
print(album1)
#Output: {'artist': 'Arjit Singn', 'title': 'Pardas'}

album2 = make_album("Salman ALI", "PardasI")
print(album2)
#OUTPUT: {'artist': 'Salman ALI', 'title': 'PardasI'}


def make_album(artis_name, album_title, no_of_track=None):
    album = {}
    album["artist"] = artis_name
    album["title"] = album_title
    if no_of_track:
        album['track'] = no_of_track
    return album
#Calling function
album3 = make_album("AR REHAMAN", "Jao ho", 50)
print(album3)
#Output: {'artist': 'AR REHAMAN', 'title': 'Jao ho', 'track': 50}

#Write a function to convert temperature from celcius to fahernheit
def to_celsius(x):
    return (x-32) * 5/9
#Call the function to check
print(to_celsius(46))

for x in range(0, 100, 10):
    print(x, to_celsius(x))

#output:
"""
0 -17.77777777777778
10 -12.222222222222221
20 -6.666666666666667
30 -1.1111111111111112
40 4.444444444444445
50 10.0
60 15.555555555555555
70 21.11111111111111
80 26.666666666666668
90 32.22222222222222
"""