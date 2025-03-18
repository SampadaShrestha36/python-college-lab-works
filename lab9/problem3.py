# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.

class Student:
    student_name='Sampada'
    marks=100
s1=Student()
print(s1.student_name)
print(s1.marks)
s1.student_name='Shrestha'
s1.marks=100
print(s1.student_name)
print(s1.marks)