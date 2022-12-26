#List is collection which is ordered and changeabel. List allows duplicate members
#empty list
my_list = []
#list with integer values
list1 = [1,2,3,4,5,]
print(list1)

#List with float values
list_float = [1.5, 2.5, 2.9, 3.0]
print(list_float)

#list of string valuse as following
list_string = ["python", "java", "c", "c#"]
print(list_string)
print(type(list_string))

#list with mixed datatypes
mix_list = [1, 1.5, "python"]
print(mix_list)

#Nested list 
nested_list = [1, 2, [3,4,5]]
print(nested_list)

mixed_nested_list = [1, 2, ['mango', "banana"], 5.5]
print(mixed_nested_list)


#Accessing specific element of list (indexing)
my_list = [1, 2, 3, 4, 5, 6]
print(my_list[4])
#it will display 5 as list indexing start with 0


# Nested indexing
my_list = ["Mitch", [3, 6, 7], ["yellow", 5, 6]]
print(my_list)

sub_list = my_list[1]
print(sub_list)
#Now it will display [3,6,7] the whole list is in index 1

#Checking while an element is in the list or not
print(6 in my_list)
# it will display boolean out as for this condition it will display "False"


#As far the list has positive indexing as well as negative indexing
print(my_list[-1])
#It will display last element of the list

#List slicing 
my_new_list = [1,2,3,4,5,6,7,8,9]
#imy_new_list has 9 elements but last element has index of 10

print(my_new_list[1:4])
#output : [2, 3, 4] it has simple rule as first element 1 has starter which include and last 4 which are excluded


#element 4th to the end
print(my_new_list[4 :])

#element from start to end
print(my_new_list[:])

print(len(my_new_list)) #9

#Adding new member to existing list
# 1. Adding member to the last of the existing list we will use append() method
#for example we have list my_new_list which has 9 element so we are going to add 10th elements.