#Dictionary is the data type in python which has value and key combination in a pair. which is in close in square braket.
this_is_dict = {}
print(type(this_is_dict))
#this has display <class 'dict'>

#let have create student dictionary which has student dictionary

student  = {
    "f_name" : "Hassan",
    "l_name" : "Ali",
    "roll_num" : "kiu-1099",
    "email" : "hassan@kiu.edu.pk",
    "semester" : "8th"
}
print(student)
#here f_name is key and "Hassan" is a value which has key value pair.


# if we iterate directly on dictionary it will return keys only
for i in student:
    print(i)
#It will return all keys in dictionary

# if we iterate on dictionary.keys() it will return keys.
for i in student.keys():
    print(i)

#we will get values directly
for j in student.values():
    print(j)

# we can get values directly
for vals in student.values():
    print(vals)
#we can also print both values and keys both

for key , value in student.items():
    print(key, value)
#.item will print both key and item.