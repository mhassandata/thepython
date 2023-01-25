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
# for example we have list my_new_list which has 9 element so we are going to add 10th elements.
# for example we have to add element in any postition we have method insert()

my_new_list.append(10)
print(my_new_list)
#The out will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_new_list.insert(11, 12)
print(my_new_list)
#output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
#But we will position the element in any index 
my_new_list.insert(2, 100)
print(my_new_list)
#output: [1, 2, 100, 3, 4, 5, 6, 7, 8, 9, 10, 12]


#Removing members from existing list
# del commmand
# remove function
# pop function
del my_new_list[-1]
print(my_new_list)
#output: [1, 2, 100, 3, 4, 5, 6, 7, 8, 9, 10]

my_new_list.remove(100)
print(my_new_list)
#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Pop() removes a members permanently but it returns the removed
so that you can utilize it later if u need it.
By defauly pop() removes value from end of the list But if you supply index like:
pop(3) it will remove the same index value"""
 
my_new_list.pop()
print(my_new_list)
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



#Slicing a List
# Slice basically copies and return the part of list 
my_new_list.sort(reverse=False)
print(my_new_list)

print(my_new_list[1:4])
#Output: [2, 3, 4]
#While sclicing here the one is included starter point and end is not included 4
#But slice has third point called step which tell the python to slice the list step wise 
#Example
print(my_new_list[0:8:2])
# In this case the output [1, 3, 5, 7]


# Advance comprehension
## Conditionals in comprehension

my_com_list = [num **2 for num in range(10) if num % 2 ==0]
print(my_com_list)
#ouput: [0, 4, 16, 36, 64]
my_com_list_1 = [num ** 2 if num % 2 ==0 else 0 for num in range(10)]
print(my_com_list_1)
#output: [0, 0, 4, 0, 16, 0, 36, 0, 64, 0]


new_list = [1,2,3,4]
mul = {i: 3*i for i in new_list}
print(mul)
#output: {1: 3, 2: 6, 3: 9, 4: 12}

mix_list = [5, "M", 6, "N", "O", 8]
integers = [j if type(j) == int else 0 for j in mix_list]
print(integers)
#output: [5, 0, 6, 0, 0, 8]