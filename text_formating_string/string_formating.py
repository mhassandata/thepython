#Formating string has many types simple string concatenating format, dot format method sequence wise and f format.

student_name = "Hassan"
student_father_name = "M Hasil Khan"
batch = '37'
university_name = "PIAIC"
age = 27
gender = "Male"
date_of_admission = "2022-06-01"
class_timing = '09:00 to 12:00'

student_card = """
    *****************Student Card*****************************
    Name of Student: """+str(student_name)+"""
    Name of Student's Father's name : """+str(student_father_name)+"""
    Batch of Enrollment: """+str(batch)+"""
    Name of University: """+str(university_name)+"""
    Age of Student: """+str(age)+"""
    Date of Addmission Student: """+str(date_of_admission)+"""
    Class timing: """+str(class_timing)+"""

    *****************END*****************************************
"""
print(student_card)

#formation with .format string method (sequance wise)
student_card_1 = """
    *****************Student Card_1*****************************
    Name of Student: {}
    Name of Student's Father's name : {}
    Batch of Enrollment: {}
    Name of University: {}
    Age of Student: {}
    Date of Addmission Student:{}
    Class timing: {}
    *****************END*****************************************
    """.format(student_name, student_father_name, batch, university_name, age, date_of_admission, class_timing)
print(student_card_1)



#Now the latest method called f format

student_card_2 = f"""
    *****************Student Card_2*****************************
    Name of Student: {student_name}
    Name of Student's Father's name : {student_father_name}
    Batch of Enrollment: {batch}
    Name of University: {university_name}
    Age of Student: {age}
    Date of Addmission Student:{date_of_admission}
    Class timing: {class_timing}
    *****************END*****************************************
    """
print(student_card_2)

"""
Output:
     *****************Student Card_2*****************************
    Name of Student: Hassan
    Name of Student's Father's name : M Hasil Khan
    Batch of Enrollment: 37
    Name of University: PIAIC
    Age of Student: 27
    Date of Addmission Student:2022-06-01
    Class timing: 09:00 to 12:00
    *****************END*****************************************



"""